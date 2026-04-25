"""Tests for the data loader module."""

import os

import pytest

from src.data_loader import LegalDataset, load_dataset, get_splits, get_statistics


class TestLoadDataset:
    def test_load_dataset_returns_list(self, tmp_dataset_file):
        data = load_dataset(tmp_dataset_file)
        assert isinstance(data, list)

    def test_load_dataset_correct_count(self, tmp_dataset_file):
        data = load_dataset(tmp_dataset_file)
        assert len(data) == 12

    def test_load_dataset_record_has_required_keys(self, tmp_dataset_file):
        data = load_dataset(tmp_dataset_file)
        for record in data:
            assert "uid" in record
            assert "doc" in record
            assert "original_text" in record
            assert "reference_summary" in record


class TestGetSplits:
    def test_splits_have_correct_keys(self, sample_dataset):
        splits = get_splits(sample_dataset)
        assert "train" in splits
        assert "val" in splits
        assert "test" in splits

    def test_splits_cover_all_data(self, sample_dataset):
        splits = get_splits(sample_dataset)
        total = len(splits["train"]) + len(splits["val"]) + len(splits["test"])
        assert total == len(sample_dataset)

    def test_splits_no_overlap(self, sample_dataset):
        splits = get_splits(sample_dataset)
        train_uids = {r["uid"] for r in splits["train"]}
        val_uids = {r["uid"] for r in splits["val"]}
        test_uids = {r["uid"] for r in splits["test"]}
        assert len(train_uids & val_uids) == 0
        assert len(train_uids & test_uids) == 0
        assert len(val_uids & test_uids) == 0

    def test_splits_approximate_ratios(self, sample_dataset):
        splits = get_splits(sample_dataset, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1)
        n = len(sample_dataset)
        # Allow some rounding tolerance
        assert len(splits["train"]) == int(n * 0.8)
        assert len(splits["val"]) == int(n * 0.1)

    def test_splits_reproducible(self, sample_dataset):
        splits1 = get_splits(sample_dataset, seed=42)
        splits2 = get_splits(sample_dataset, seed=42)
        assert [r["uid"] for r in splits1["train"]] == [r["uid"] for r in splits2["train"]]


class TestGetStatistics:
    def test_statistics_keys(self, sample_dataset):
        stats = get_statistics(sample_dataset)
        assert "record_count" in stats
        assert "avg_original_length" in stats
        assert "avg_summary_length" in stats
        assert "sources" in stats

    def test_statistics_record_count(self, sample_dataset):
        stats = get_statistics(sample_dataset)
        assert stats["record_count"] == len(sample_dataset)

    def test_statistics_lengths_positive(self, sample_dataset):
        stats = get_statistics(sample_dataset)
        assert stats["avg_original_length"] > 0
        assert stats["avg_summary_length"] > 0

    def test_statistics_sources_are_unique(self, sample_dataset):
        stats = get_statistics(sample_dataset)
        assert len(stats["sources"]) == len(set(stats["sources"]))

    def test_statistics_empty_data(self):
        stats = get_statistics([])
        assert stats["record_count"] == 0


class TestRealDatasets:
    """Test loading the actual dataset files."""

    @pytest.mark.skipif(
        not os.path.exists("all_v1.json"),
        reason="all_v1.json not found",
    )
    def test_load_all_v1(self):
        data = load_dataset("all_v1.json")
        assert len(data) == 446
        for record in data[:5]:
            assert "original_text" in record
            assert "reference_summary" in record

    @pytest.mark.skipif(
        not os.path.exists("tldrlegal_v1.json"),
        reason="tldrlegal_v1.json not found",
    )
    def test_load_tldrlegal_v1(self):
        data = load_dataset("tldrlegal_v1.json")
        assert len(data) == 85

    @pytest.mark.skipif(
        not os.path.exists("tosdr_annotated_v1.json"),
        reason="tosdr_annotated_v1.json not found",
    )
    def test_load_tosdr_annotated_v1(self):
        data = load_dataset("tosdr_annotated_v1.json")
        assert len(data) == 361
