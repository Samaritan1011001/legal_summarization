"""Module for loading and analyzing legal text summarization datasets.

Provides utilities to load JSON dataset files and compute basic summary
statistics over the loaded entries.
"""

from __future__ import annotations

import json
import os
from typing import Any, TypedDict, Union


class DatasetEntry(TypedDict, total=False):
    """Schema for a single dataset entry.

    Required fields (present in every entry):
        uid: Unique identifier for the entry.
        original_text: The original legal text.
        reference_summary: The reference (gold) summary.
        doc: The document name or title of the source.

    Optional fields (vary by dataset source):
        id: Source-specific identifier.
        title: Section or clause title.
        note: Annotation note.
        urls: Related URLs.
        case_code: ToS;DR case classification code.
        case_text: ToS;DR case classification text.
        title_code: ToS;DR title classification code.
        title_text: ToS;DR title classification text.
        tldr_code: ToS;DR TLDR classification code.
        tldr_text: ToS;DR TLDR classification text.
    """

    # Required fields
    uid: str
    original_text: str
    reference_summary: str
    doc: str

    # Optional fields
    id: str
    title: str
    note: str
    urls: list[str]
    case_code: str
    case_text: str
    title_code: str
    title_text: str
    tldr_code: str
    tldr_text: str


def load_dataset(filepath: str) -> list[dict[str, Any]]:
    """Load a JSON dataset file and return its entries as a list of dicts.

    Each JSON file is expected to be a dictionary keyed by entry identifiers,
    where each value is a dictionary representing a single dataset entry.

    Args:
        filepath: Path to the JSON dataset file.

    Returns:
        A list of dataset entry dictionaries.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw: dict[str, Any] = json.load(f)
    return list(raw.values())


def get_summary_stats(data: list[dict[str, Any]]) -> dict[str, Union[int, float]]:
    """Compute basic statistics over a list of dataset entries.

    Args:
        data: A list of dataset entry dictionaries. Each entry is expected
            to contain ``original_text`` and ``reference_summary`` keys.

    Returns:
        A dictionary with the following keys:

        - ``count``: Total number of entries.
        - ``avg_original_text_length``: Mean character length of original texts.
        - ``avg_summary_length``: Mean character length of reference summaries.
    """
    count: int = len(data)
    if count == 0:
        return {
            "count": 0,
            "avg_original_text_length": 0.0,
            "avg_summary_length": 0.0,
        }

    total_original: int = sum(len(entry.get("original_text", "")) for entry in data)
    total_summary: int = sum(len(entry.get("reference_summary", "")) for entry in data)

    return {
        "count": count,
        "avg_original_text_length": round(total_original / count, 2),
        "avg_summary_length": round(total_summary / count, 2),
    }


if __name__ == "__main__":
    dataset_path: str = os.path.join(os.path.dirname(__file__), "all_v1.json")
    entries: list[dict[str, Any]] = load_dataset(dataset_path)
    stats: dict[str, Union[int, float]] = get_summary_stats(entries)

    print(f"Loaded {stats['count']} entries from all_v1.json")
    print(f"  Avg original text length: {stats['avg_original_text_length']} chars")
    print(f"  Avg summary length:       {stats['avg_summary_length']} chars")
