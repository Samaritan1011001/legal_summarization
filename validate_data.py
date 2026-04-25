#!/usr/bin/env python3
"""Simple data validation utility for the legal_summarization dataset.

Loads each JSON file, counts the number of top-level entries, checks for
expected fields, and prints a summary.
"""

import json
import os
import sys

# Dataset files and their expected entry counts
DATASET_FILES = {
    "all_v1.json": 446,
    "tldrlegal_v1.json": 85,
    "tosdr_annotated_v1.json": 361,
}

# Required fields per dataset file (fields common to all entries in each file)
REQUIRED_FIELDS = {
    "all_v1.json": ["doc", "original_text", "reference_summary", "uid"],
    "tldrlegal_v1.json": ["doc", "id", "original_text", "reference_summary", "title", "uid"],
    "tosdr_annotated_v1.json": [
        "doc",
        "note",
        "original_text",
        "reference_summary",
        "uid",
        "urls",
    ],
}


def validate_file(filepath, expected_count, required_fields):
    """Validate a single JSON dataset file.

    Returns a dict with validation results.
    """
    results = {
        "file": filepath,
        "exists": False,
        "valid_json": False,
        "entry_count": 0,
        "expected_count": expected_count,
        "count_match": False,
        "missing_fields": {},
        "errors": [],
    }

    if not os.path.isfile(filepath):
        results["errors"].append("File not found")
        return results
    results["exists"] = True

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        results["errors"].append(f"Invalid JSON: {e}")
        return results
    results["valid_json"] = True

    if not isinstance(data, dict):
        results["errors"].append(f"Expected a JSON object (dict), got {type(data).__name__}")
        return results

    results["entry_count"] = len(data)
    results["count_match"] = len(data) == expected_count

    # Check required fields in each entry
    for key, entry in data.items():
        if not isinstance(entry, dict):
            results["errors"].append(f"Entry '{key}' is not a dict")
            continue
        missing = [field for field in required_fields if field not in entry]
        if missing:
            results["missing_fields"][key] = missing

    return results


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_passed = True

    print("=" * 60)
    print("Legal Summarization Dataset Validation")
    print("=" * 60)

    for filename, expected_count in DATASET_FILES.items():
        filepath = os.path.join(base_dir, filename)
        required_fields = REQUIRED_FIELDS[filename]
        results = validate_file(filepath, expected_count, required_fields)

        status = "PASS" if (
            results["exists"]
            and results["valid_json"]
            and results["count_match"]
            and not results["missing_fields"]
            and not results["errors"]
        ) else "FAIL"

        if status == "FAIL":
            all_passed = False

        print(f"\n[{status}] {filename}")
        print(f"  Entries: {results['entry_count']} (expected {results['expected_count']})")

        if not results["exists"]:
            print("  ERROR: File not found")
        elif not results["valid_json"]:
            print("  ERROR: Invalid JSON")
        elif not results["count_match"]:
            print(f"  ERROR: Entry count mismatch")

        if results["missing_fields"]:
            count = len(results["missing_fields"])
            print(f"  WARNING: {count} entries with missing fields")
            # Show first few examples
            for key in list(results["missing_fields"].keys())[:3]:
                print(f"    '{key}' missing: {results['missing_fields'][key]}")
            if count > 3:
                print(f"    ... and {count - 3} more")

        for error in results["errors"]:
            print(f"  ERROR: {error}")

    print("\n" + "=" * 60)
    if all_passed:
        print("All validations passed.")
    else:
        print("Some validations failed.")
    print("=" * 60)

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
