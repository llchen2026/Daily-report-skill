#!/usr/bin/env python3
"""
Fetch energy & chemical commodity prices from akshare.
Outputs a structured JSON file with latest prices, changes, and crack spreads.
"""

import json
import sys
import os
from datetime import datetime, timedelta

import akshare as ak


# ============================================================
# 能化期货品种映射表
# ============================================================
# 格式: sina_code -> (中文名, 品种类别, 产业链位置)
FUTURES_MAP = {
    # 原油/燃料油
    "SC0":  ("INE原油",      "crude",     "upstream"),
    "FU0":  ("燃料油",        "fueloil",   "midstream"),
    "LU0":  ("低硫燃料油",    "fueloil",   "midstream"),
    "BU0":  ("沥青",          "asphalt",   "midstream"),
    # 烯烃链
    "PP0":  ("聚丙烯",        "olefin",    "downstream"),
    "L0":   ("线性PE",        "olefin",    "downstream"),
    "EB0":  ("苯乙烯",        "aromatic",  "downstream"),
    "EG0":  ("乙二醇",        "olefin",    "downstream"),
    # 芳烃/PTA
    "TA0":  ("PTA",           "aromatic",  "downstream"),
    "PX0":  ("对二甲苯",      "aromatic",  "midstream"),
    "PR0":  ("瓶片",          "polymer",   "downstream"),
    # 醇类
    "MA0":  ("甲醇",          "alcohol",   "midstream"),
    # 氯碱/聚氨酯
    "V0":   ("PVC",           "chlorine",  "downstream"),
    "SA0":  ("纯碱",          "chlorine",  "midstream"),
    # 其他
    "PG0":  ("LPG",           "gas",       "midstream"),
    "SP0":  ("短纤",          "fiber",     "downstream"),
    "RU0":  ("橡胶",          "rubber",    "downstream"),
    "NR0":  ("20号胶",        "rubber",    "downstream"),
}


def fetch_futures_daily():
    """Fetch latest daily OHLC for all mapped futures contracts."""
    results = []
    today_str = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    for code, (name, category, position) in FUTURES_MAP.items():
        try:
            df = ak.futures_zh_daily_sina(symbol=code)
            if df.empty:
                continue
            latest = df.tail(1).iloc[0]
            prev = df.tail(2).iloc[0] if len(df) >= 2 else latest

            close = float(latest["close"])
            prev_close = float(prev["close"])
            change = close - prev_close
            change_pct = (change / prev_close * 100) if prev_close else 0.0

            results.append({
                "code": code,
                "name": name,
                "category": category,
                "position": position,
                "date": str(latest["date"]),
                "open": float(latest["open"]),
                "high": float(latest["high"]),
                "low": float(latest["low"]),
                "close": close,
                "settle": float(latest["settle"]),
                "volume": int(latest["volume"]),
                "hold": int(latest["hold"]),
                "change": round(change, 2),
                "change_pct": round(change_pct, 2),
            })
        except Exception as e:
            results.append({
                "code": code,
                "name": name,
                "category": category,
                "position": position,
                "error": str(e),
            })

    return results


def fetch_product_oil_price():
    """Fetch China product oil price adjustment history."""
    try:
        df = ak.energy_oil_hist()
        latest = df.tail(1).iloc[0]
        return {
            "adjust_date": str(latest["调整日期"]),
            "gasoline_price": int(latest["汽油价格"]),
            "diesel_price": int(latest["柴油价格"]),
            "gasoline_change": float(latest["汽油涨跌"]),
            "diesel_change": float(latest["柴油涨跌"]),
        }
    except Exception as e:
        return {"error": str(e)}


def fetch_eia_crude():
    """Fetch latest EIA crude oil inventory data."""
    try:
        df = ak.macro_usa_eia_crude_rate()
        latest = df.tail(1).iloc[0]
        return {
            "date": str(latest["日期"]),
            "actual": float(latest["今值"]) if str(latest["今值"]) != "nan" else None,
            "forecast": float(latest["预测值"]) if str(latest["预测值"]) != "nan" else None,
            "previous": float(latest["前值"]) if str(latest["前值"]) != "nan" else None,
        }
    except Exception as e:
        return {"error": str(e)}


def compute_crack_spreads(futures_data):
    """Compute approximate crack spreads relative to SC (crude)."""
    sc_price = None
    for f in futures_data:
        if f.get("code") == "SC0" and "close" in f:
            sc_price = f["close"]
            break

    if not sc_price:
        return {}

    # SC原油单位是元/桶, 其他品种是元/吨
    # 粗略换算: 1吨原油 ≈ 7.33桶
    sc_per_ton = sc_price * 7.33

    spreads = {}
    for f in futures_data:
        if "close" not in f or f["code"] == "SC0":
            continue
        product_price = f["close"]
        spread = product_price - sc_per_ton
        spreads[f["code"]] = {
            "name": f["name"],
            "spread": round(spread, 2),
            "spread_pct": round(spread / sc_per_ton * 100, 2),
        }

    return spreads


def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    output_file = os.path.join(output_dir, ".akshare-data.json")

    print("Fetching futures daily data...")
    futures = fetch_futures_daily()

    print("Fetching product oil prices...")
    product_oil = fetch_product_oil_price()

    print("Fetching EIA crude inventory...")
    eia = fetch_eia_crude()

    print("Computing crack spreads...")
    cracks = compute_crack_spreads(futures)

    result = {
        "fetch_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "futures": futures,
        "product_oil": product_oil,
        "eia_crude": eia,
        "crack_spreads_vs_sc": cracks,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Data saved to: {output_file}")

    # Print summary
    print("\n=== 期货价格摘要 ===")
    for item in futures:
        if "close" in item:
            arrow = "↑" if item["change"] > 0 else "↓" if item["change"] < 0 else "→"
            print(f"  {item['name']:8s} ({item['code']}): {item['close']:>8.1f}  {arrow} {item['change_pct']:+.2f}%")

    print(f"\n=== 成品油调价 ===")
    if "gasoline_price" in product_oil:
        print(f"  汽油: {product_oil['gasoline_price']}  柴油: {product_oil['diesel_price']}")

    print(f"\n=== EIA库存 ===")
    if "actual" in eia and eia["actual"] is not None:
        print(f"  最新值: {eia['actual']}  预测: {eia['forecast']}  前值: {eia['previous']}")


if __name__ == "__main__":
    main()
