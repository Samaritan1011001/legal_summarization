"""Typed utility helpers for loading and querying the Legal Summarization dataset.

The dataset files (``all_v1.json``, ``tldrlegal_v1.json``,
``tosdr_annotated_v1.json``) are JSON objects keyed by a unique identifier
(uid).  Each value is a record with the following string fields:

* **uid** -- unique identifier (e.g. ``"legalsum01"``)
* **id** -- source identifier
* **doc** -- document / service name
* **title** -- title of the legal document
* **original_text** -- full text of the legal document
* **reference_summary** -- plain-English summary
"""

import json
from typing import Dict, List, Optional, TypedDict


class LegalEntry(TypedDict):
    """A single record in the legal-summarization dataset."""

    uid: str
    id: str
    doc: str
    title: str
    original_text: str
    reference_summary: str


# The top-level structure of every dataset file: uid -> entry.
Dataset = Dict[str, LegalEntry]


def load_dataset(file_path: str) -> Dataset:
    """Load a legal-summarization JSON dataset from *file_path*.

    Parameters
    ----------
    file_path:
        Path to one of the dataset JSON files (e.g. ``"all_v1.json"``).

    Returns
    -------
    Dataset
        A dictionary mapping each uid to its :class:`LegalEntry`.

    Raises
    ------
    FileNotFoundError
        If *file_path* does not exist.
    json.JSONDecodeError
        If the file contains invalid JSON.
    """
    with open(file_path, "r", encoding="utf-8") as fh:
        data: Dataset = json.load(fh)
    return data


def get_summary(dataset: Dataset, uid: str) -> Optional[str]:
    """Return the reference summary for *uid*, or ``None`` if not found.

    Parameters
    ----------
    dataset:
        A dataset previously loaded via :func:`load_dataset`.
    uid:
        The unique identifier of the entry (e.g. ``"legalsum01"``).

    Returns
    -------
    Optional[str]
        The plain-English reference summary, or ``None`` when the uid
        does not exist in the dataset.
    """
    entry: Optional[LegalEntry] = dataset.get(uid)
    if entry is None:
        return None
    return entry["reference_summary"]


def list_uids(dataset: Dataset) -> List[str]:
    """Return a sorted list of all uids present in *dataset*.

    Parameters
    ----------
    dataset:
        A dataset previously loaded via :func:`load_dataset`.

    Returns
    -------
    List[str]
        Sorted uid strings.
    """
    return sorted(dataset.keys())


def get_entry(dataset: Dataset, uid: str) -> Optional[LegalEntry]:
    """Return the full entry for *uid*, or ``None`` if not found.

    Parameters
    ----------
    dataset:
        A dataset previously loaded via :func:`load_dataset`.
    uid:
        The unique identifier of the entry.

    Returns
    -------
    Optional[LegalEntry]
        The complete record, or ``None`` when the uid does not exist.
    """
    return dataset.get(uid)
