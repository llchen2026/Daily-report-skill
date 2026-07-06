#!/usr/bin/env python3
"""
News deduplication and store management.
Reads standardized news records, deduplicates by hash, writes to JSONL store.
"""

import json
import os
import sys
import hashlib
from datetime import datetime, timedelta
from pathlib import Path


def compute_dedup_hash(record: dict) -> str:
    """Compute dedup hash from entities + event_type + value_change metric + date."""
    entities = record.get("entities", {})
    entity_set = set()
    for v in entities.values():
        if isinstance(v, list):
            entity_set.update(v)
        elif isinstance(v, str):
            entity_set.add(v)
    sorted_entities = "|".join(sorted(entity_set))

    event_type = record.get("event_type", "")
    metric = record.get("value_change", {}).get("metric", "") if record.get("value_change") else ""
    date_str = record.get("publish_time", "")[:10]  # date level granularity

    raw = f"{sorted_entities}|{event_type}|{metric}|{date_str}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def load_existing_hashes(store_dir: str, months_back: int = 2) -> set:
    """Load dedup hashes from recent monthly JSONL files."""
    existing_hashes = set()
    now = datetime.now()

    for i in range(months_back):
        month_date = now - timedelta(days=30 * i)
        filename = month_date.strftime("%Y-%m") + ".jsonl"
        filepath = os.path.join(store_dir, filename)

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        record = json.loads(line)
                        h = record.get("dedup_hash", "")
                        if h:
                            existing_hashes.add(h)
                    except json.JSONDecodeError:
                        continue

    return existing_hashes


def deduplicate_news(news_records: list, store_dir: str) -> tuple:
    """
    Deduplicate news records against existing store.
    Returns (unique_records, duplicate_count).
    """
    existing_hashes = load_existing_hashes(store_dir)

    unique = []
    seen_in_batch = set()
    dup_count = 0

    for record in news_records:
        h = compute_dedup_hash(record)
        record["dedup_hash"] = h

        if h in existing_hashes or h in seen_in_batch:
            dup_count += 1
            continue

        seen_in_batch.add(h)
        unique.append(record)

    return unique, dup_count


def append_to_store(records: list, store_dir: str) -> str:
    """Append unique records to the current month's JSONL file."""
    os.makedirs(store_dir, exist_ok=True)
    current_month = datetime.now().strftime("%Y-%m")
    filepath = os.path.join(store_dir, f"{current_month}.jsonl")

    with open(filepath, "a", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return filepath


def load_recent_records(store_dir: str, days_back: int = 30) -> list:
    """Load recent records for baseline tracking."""
    records = []
    cutoff = datetime.now() - timedelta(days=days_back)

    for filepath in sorted(Path(store_dir).glob("*.jsonl"), reverse=True):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    pub_time = record.get("publish_time", "")
                    if pub_time:
                        record_date = datetime.fromisoformat(pub_time)
                        if record_date >= cutoff:
                            records.append(record)
                except (json.JSONDecodeError, ValueError):
                    continue

    return records


def main():
    """
    CLI: python3 deduplicate_news.py <input.json> <store_dir>

    input.json: a JSON array of standardized news records (without dedup_hash)
    store_dir: directory for monthly JSONL files
    """
    if len(sys.argv) < 3:
        print("Usage: deduplicate_news.py <input.json> <store_dir>")
        sys.exit(1)

    input_file = sys.argv[1]
    store_dir = sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        news_records = json.load(f)

    unique, dup_count = deduplicate_news(news_records, store_dir)

    if unique:
        filepath = append_to_store(unique, store_dir)
        print(f"Wrote {len(unique)} unique records to {filepath}")
    else:
        print("No unique records to write.")

    print(f"Deduplicated: {dup_count} duplicates removed out of {len(news_records)} total.")


if __name__ == "__main__":
    main()
