#!/usr/bin/env python3
"""
Generate investment view dashboard HTML from analysis results.
Replaces template placeholders with actual data, saves to output directory.
"""

import json
import os
import sys
from datetime import datetime


def generate_dashboard(data: dict, output_dir: str) -> str:
    """
    Generate the final dashboard HTML file.

    Args:
        data: dict with keys matching template placeholders (without __ delimiters)
        output_dir: directory to write the output HTML file

    Returns:
        Path to the generated HTML file.
    """
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets", "dashboard-template.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Fill in all placeholders
    for key, value in data.items():
        placeholder = f"__{key.upper()}__"
        html = html.replace(placeholder, str(value))

    # Write output
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"oil-intel-dashboard-{timestamp}.html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    return output_file


if __name__ == "__main__":
    # When called directly, accept a JSON data file as input
    if len(sys.argv) < 3:
        print("Usage: generate_dashboard.py <data.json> <output_dir>")
        sys.exit(1)

    data_file = sys.argv[1]
    output_dir = sys.argv[2]

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = generate_dashboard(data, output_dir)
    print(f"Dashboard generated: {result}")
