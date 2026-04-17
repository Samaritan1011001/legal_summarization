"""Tests for data_loader module."""

import json
import tempfile
from pathlib import Path

import pytest

from src.data_loader import load_dataset, load_all_datasets, get_sample


@pytest.fixture
def sample_dataset():
    """Create a sample dataset for testing."""
    return {
        "doc1": {
            "uid": "doc1",
            "original_text": "This is the original legal text for document one.",
            "reference_summary": "Summary of document one.",
            "doc": "Test Document 1",
            "title": "Title 1",
        },
        "doc2": {
            "uid": "doc2",
            "original_text": "This is another legal document with different content.",
            "reference_summary": "Summary of document two.",
            "doc": "Test Document 2",
            "title": "",
        },
    }


@pytest.fixture
def temp_dataset_file(sample_dataset):
    """Create a temporary dataset file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(sample_dataset, f)
        return Path(f.name)


def test_load_dataset(temp_dataset_file):
    """Test loading a dataset from a JSON file."""
    docs = load_dataset(temp_dataset_file)
    
    assert len(docs) == 2
    assert all("uid" in doc for doc in docs)
    assert all("original_text" in doc for doc in docs)
    assert all("reference_summary" in doc for doc in docs)


def test_load_dataset_file_not_found():
    """Test that FileNotFoundError is raised for missing files."""
    with pytest.raises(FileNotFoundError):
        load_dataset("nonexistent_file.json")


def test_get_sample(temp_dataset_file):
    """Test getting a sample from the dataset."""
    docs = load_dataset(temp_dataset_file)
    
    # Test random sample
    sample = get_sample(docs)
    assert sample in docs
    
    # Test specific index
    sample = get_sample(docs, index=0)
    assert sample == docs[0]


def test_get_sample_empty_dataset():
    """Test that ValueError is raised for empty dataset."""
    with pytest.raises(ValueError):
        get_sample([])


def test_get_sample_index_out_of_range(temp_dataset_file):
    """Test that IndexError is raised for out of range index."""
    docs = load_dataset(temp_dataset_file)
    
    with pytest.raises(IndexError):
        get_sample(docs, index=100)


def test_load_real_dataset():
    """Test loading the actual all_v1.json dataset."""
    data_dir = Path(__file__).parent.parent
    dataset_path = data_dir / "all_v1.json"
    
    if dataset_path.exists():
        docs = load_dataset(dataset_path)
        assert len(docs) > 0
        
        # Check structure of first document
        doc = docs[0]
        assert "uid" in doc
        assert "original_text" in doc
        assert "reference_summary" in doc
        assert "doc" in doc
