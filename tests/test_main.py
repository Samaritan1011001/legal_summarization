"""Tests for the main pipeline module."""

import json
import os
from argparse import Namespace
from unittest.mock import patch, MagicMock

import pytest

from src.main import run_pipeline, parse_args


@pytest.fixture
def mock_summarizer_class():
    """Mock the LegalSummarizer to avoid model downloads."""
    with patch("src.main.LegalSummarizer") as mock_cls:
        mock_instance = MagicMock()
        mock_cls.return_value = mock_instance
        mock_instance.summarize_batch.return_value = [
            "this is a mock summary for testing purposes"
        ]
        yield mock_cls, mock_instance


class TestParseArgs:
    def test_default_args(self):
        with patch("sys.argv", ["main.py"]):
            args = parse_args()
            assert args.dataset == "all_v1.json"
            assert args.model == "facebook/bart-large-cnn"
            assert args.max_samples is None
            assert args.output_dir == "results/"
            assert args.batch_size == 4

    def test_custom_args(self):
        with patch("sys.argv", [
            "main.py",
            "--dataset", "test.json",
            "--model", "t5-small",
            "--max_samples", "5",
            "--output_dir", "out/",
            "--batch_size", "2",
        ]):
            args = parse_args()
            assert args.dataset == "test.json"
            assert args.model == "t5-small"
            assert args.max_samples == 5
            assert args.output_dir == "out/"
            assert args.batch_size == 2


class TestRunPipeline:
    def test_end_to_end_with_mock(self, tmp_dataset_file, mock_summarizer_class, tmp_path):
        mock_cls, mock_instance = mock_summarizer_class

        # Make summarize_batch return one summary per input text
        def fake_summarize_batch(texts, batch_size=4, **kwargs):
            return ["mock summary" for _ in texts]

        mock_instance.summarize_batch.side_effect = fake_summarize_batch

        output_dir = str(tmp_path / "results")
        args = Namespace(
            dataset=tmp_dataset_file,
            model="facebook/bart-large-cnn",
            max_samples=2,
            output_dir=output_dir,
            batch_size=4,
        )

        run_pipeline(args)

        # Verify results file was created
        results_path = os.path.join(output_dir, "results.json")
        assert os.path.exists(results_path)

        # Verify results content
        with open(results_path) as f:
            results = json.load(f)

        assert results["num_samples"] == 2
        assert "results" in results
        assert "rouge_scores" in results["results"]
        assert "statistics" in results["results"]
        assert len(results["predictions"]) == 2

    def test_pipeline_without_max_samples(self, tmp_dataset_file, mock_summarizer_class, tmp_path):
        mock_cls, mock_instance = mock_summarizer_class

        def fake_summarize_batch(texts, batch_size=4, **kwargs):
            return ["mock summary" for _ in texts]

        mock_instance.summarize_batch.side_effect = fake_summarize_batch

        output_dir = str(tmp_path / "results2")
        args = Namespace(
            dataset=tmp_dataset_file,
            model="facebook/bart-large-cnn",
            max_samples=None,
            output_dir=output_dir,
            batch_size=4,
        )

        run_pipeline(args)

        results_path = os.path.join(output_dir, "results.json")
        assert os.path.exists(results_path)

        with open(results_path) as f:
            results = json.load(f)

        # Without max_samples, test split should have some records
        assert results["num_samples"] > 0
