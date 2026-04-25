"""Tests for the preprocessing module."""

from unittest.mock import MagicMock

import pytest

from src.preprocessing import TextPreprocessor


@pytest.fixture
def preprocessor():
    return TextPreprocessor()


class TestCleanText:
    def test_normalizes_whitespace(self, preprocessor):
        text = "hello   world   foo"
        assert preprocessor.clean_text(text) == "hello world foo"

    def test_strips_leading_trailing(self, preprocessor):
        text = "  hello world  "
        assert preprocessor.clean_text(text) == "hello world"

    def test_handles_newlines_and_tabs(self, preprocessor):
        text = "hello\n\tworld\n\nfoo"
        assert preprocessor.clean_text(text) == "hello world foo"

    def test_empty_string(self, preprocessor):
        assert preprocessor.clean_text("") == ""

    def test_single_word(self, preprocessor):
        assert preprocessor.clean_text("  hello  ") == "hello"


class TestTruncateText:
    def test_truncates_long_text(self, preprocessor):
        text = " ".join(f"word{i}" for i in range(100))
        result = preprocessor.truncate_text(text, max_length=10)
        assert len(result.split()) == 10

    def test_does_not_truncate_short_text(self, preprocessor):
        text = "this is a short text"
        result = preprocessor.truncate_text(text, max_length=512)
        assert result == text

    def test_exact_length(self, preprocessor):
        text = "one two three"
        result = preprocessor.truncate_text(text, max_length=3)
        assert result == "one two three"

    def test_truncate_to_one(self, preprocessor):
        text = "one two three"
        result = preprocessor.truncate_text(text, max_length=1)
        assert result == "one"


class TestPrepareForModel:
    def test_calls_tokenizer_correctly(self, preprocessor):
        mock_tokenizer = MagicMock()
        mock_tokenizer.return_value = {"input_ids": [1, 2, 3]}
        texts = ["hello world", "foo bar"]

        result = preprocessor.prepare_for_model(texts, mock_tokenizer, max_length=256)

        mock_tokenizer.assert_called_once_with(
            texts,
            max_length=256,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )
        assert result == {"input_ids": [1, 2, 3]}

    def test_default_max_length(self, preprocessor):
        mock_tokenizer = MagicMock()
        mock_tokenizer.return_value = {}
        texts = ["test"]

        preprocessor.prepare_for_model(texts, mock_tokenizer)

        mock_tokenizer.assert_called_once_with(
            texts,
            max_length=512,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )
