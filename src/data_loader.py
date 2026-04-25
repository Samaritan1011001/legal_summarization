"""Data loading utilities for legal text summarization."""

import json
import random


class LegalDataset:
    """Dataset class for legal text summarization data."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = load_dataset(filepath)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def load_dataset(filepath):
    """Load a JSON dataset file and return a list of record dicts.

    The JSON files are dicts keyed by uid. Each value has at minimum:
    doc, original_text, reference_summary, uid.

    Args:
        filepath: Path to the JSON file.

    Returns:
        List of record dicts.
    """
    with open(filepath, "r") as f:
        data = json.load(f)
    return list(data.values())


def get_splits(data, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    """Split data into train, validation, and test sets.

    Args:
        data: List of record dicts.
        train_ratio: Fraction for training set.
        val_ratio: Fraction for validation set.
        test_ratio: Fraction for test set.
        seed: Random seed for reproducibility.

    Returns:
        Dict with 'train', 'val', 'test' lists.
    """
    data = list(data)
    rng = random.Random(seed)
    rng.shuffle(data)

    n = len(data)
    train_end = int(n * train_ratio)
    val_end = train_end + int(n * val_ratio)

    return {
        "train": data[:train_end],
        "val": data[train_end:val_end],
        "test": data[val_end:],
    }


def get_statistics(data):
    """Compute statistics about the dataset.

    Args:
        data: List of record dicts.

    Returns:
        Dict with record_count, avg_original_length, avg_summary_length, sources.
    """
    if not data:
        return {
            "record_count": 0,
            "avg_original_length": 0,
            "avg_summary_length": 0,
            "sources": [],
        }

    original_lengths = [len(r["original_text"].split()) for r in data]
    summary_lengths = [len(r["reference_summary"].split()) for r in data]
    sources = sorted(set(r["doc"] for r in data))

    return {
        "record_count": len(data),
        "avg_original_length": sum(original_lengths) / len(original_lengths),
        "avg_summary_length": sum(summary_lengths) / len(summary_lengths),
        "sources": sources,
    }
