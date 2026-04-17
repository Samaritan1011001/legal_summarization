"""Data loader for legal summarization dataset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Union


def load_dataset(filepath: Union[str, Path]) -> list[dict]:
    """Load a legal summarization dataset from a JSON file.
    
    Args:
        filepath: Path to the JSON dataset file.
        
    Returns:
        List of document dictionaries with keys: uid, original_text, 
        reference_summary, doc, and optionally title.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Dataset file not found: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Convert dict-of-dicts to list of dicts
    documents = []
    for uid, doc_data in data.items():
        doc = {
            "uid": doc_data.get("uid", uid),
            "original_text": doc_data.get("original_text", ""),
            "reference_summary": doc_data.get("reference_summary", ""),
            "doc": doc_data.get("doc", ""),
            "title": doc_data.get("title", ""),
        }
        documents.append(doc)
    
    return documents


def load_all_datasets(data_dir: Optional[Union[str, Path]] = None) -> dict[str, list[dict]]:
    """Load all available datasets from the data directory.
    
    Args:
        data_dir: Directory containing dataset files. Defaults to current directory.
        
    Returns:
        Dictionary mapping dataset names to lists of documents.
    """
    if data_dir is None:
        data_dir = Path(__file__).parent.parent
    else:
        data_dir = Path(data_dir)
    
    datasets = {}
    dataset_files = [
        "all_v1.json",
        "tldrlegal_v1.json",
        "tosdr_annotated_v1.json",
    ]
    
    for filename in dataset_files:
        filepath = data_dir / filename
        if filepath.exists():
            name = filename.replace("_v1.json", "").replace(".json", "")
            datasets[name] = load_dataset(filepath)
    
    return datasets


def get_sample(dataset: list[dict], index: Optional[int] = None) -> dict:
    """Get a sample document from the dataset.
    
    Args:
        dataset: List of document dictionaries.
        index: Optional index to select. If None, returns a random sample.
        
    Returns:
        A single document dictionary.
    """
    import random
    
    if not dataset:
        raise ValueError("Dataset is empty")
    
    if index is not None:
        if index < 0 or index >= len(dataset):
            raise IndexError(f"Index {index} out of range for dataset of size {len(dataset)}")
        return dataset[index]
    
    return random.choice(dataset)
