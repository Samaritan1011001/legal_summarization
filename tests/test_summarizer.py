"""Tests for the summarizer module (with mocked model to avoid downloads)."""

from unittest.mock import MagicMock, patch

import torch
import pytest

from src.summarizer import LegalSummarizer


@pytest.fixture
def mock_summarizer():
    """Create a LegalSummarizer with mocked model and tokenizer."""
    with patch("src.summarizer.AutoTokenizer") as mock_tok_cls, \
         patch("src.summarizer.AutoModelForSeq2SeqLM") as mock_model_cls:

        # Set up mock tokenizer
        mock_tokenizer = MagicMock()
        mock_tok_cls.from_pretrained.return_value = mock_tokenizer

        # Set up mock model
        mock_model = MagicMock()
        mock_model_cls.from_pretrained.return_value = mock_model

        # Mock tokenizer call to return tensor-like dict
        mock_tokenizer.return_value = {
            "input_ids": torch.tensor([[1, 2, 3]]),
            "attention_mask": torch.tensor([[1, 1, 1]]),
        }

        # Mock model.generate to return token ids
        mock_model.generate.return_value = torch.tensor([[0, 4, 5, 6, 2]])

        # Mock tokenizer.decode to return a summary string
        mock_tokenizer.decode.return_value = "this is a mock summary"
        mock_tokenizer.batch_decode.return_value = ["mock summary one", "mock summary two"]

        summarizer = LegalSummarizer(model_name="facebook/bart-large-cnn")

        yield summarizer, mock_tokenizer, mock_model, mock_tok_cls, mock_model_cls


class TestInit:
    def test_loads_model_and_tokenizer(self, mock_summarizer):
        summarizer, mock_tokenizer, mock_model, mock_tok_cls, mock_model_cls = mock_summarizer
        mock_tok_cls.from_pretrained.assert_called_once_with("facebook/bart-large-cnn")
        mock_model_cls.from_pretrained.assert_called_once_with("facebook/bart-large-cnn")

    def test_device_is_set(self, mock_summarizer):
        summarizer, *_ = mock_summarizer
        assert summarizer.device in ("cpu", "cuda")

    def test_model_set_to_eval(self, mock_summarizer):
        summarizer, _, mock_model, *_ = mock_summarizer
        mock_model.eval.assert_called_once()


class TestSummarize:
    def test_returns_string(self, mock_summarizer):
        summarizer, *_ = mock_summarizer
        result = summarizer.summarize("some legal text here")
        assert isinstance(result, str)

    def test_returns_expected_summary(self, mock_summarizer):
        summarizer, *_ = mock_summarizer
        result = summarizer.summarize("some legal text here")
        assert result == "this is a mock summary"

    def test_calls_generate(self, mock_summarizer):
        summarizer, _, mock_model, *_ = mock_summarizer
        summarizer.summarize("some legal text here")
        mock_model.generate.assert_called_once()


class TestSummarizeBatch:
    def test_returns_list(self, mock_summarizer):
        summarizer, *_ = mock_summarizer
        results = summarizer.summarize_batch(["text one", "text two"])
        assert isinstance(results, list)

    def test_returns_correct_count(self, mock_summarizer):
        summarizer, mock_tokenizer, mock_model, *_ = mock_summarizer
        # For batch processing, batch_decode returns 2 summaries
        mock_tokenizer.batch_decode.return_value = ["summary one", "summary two"]
        results = summarizer.summarize_batch(["text one", "text two"], batch_size=4)
        assert len(results) == 2

    def test_handles_multiple_batches(self, mock_summarizer):
        summarizer, mock_tokenizer, mock_model, *_ = mock_summarizer
        texts = ["text one", "text two", "text three"]
        # First batch of 2, second batch of 1
        mock_tokenizer.batch_decode.side_effect = [
            ["summary one", "summary two"],
            ["summary three"],
        ]
        results = summarizer.summarize_batch(texts, batch_size=2)
        assert len(results) == 3
