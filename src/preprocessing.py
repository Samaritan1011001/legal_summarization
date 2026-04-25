"""Text preprocessing utilities for legal text summarization."""

import re


class TextPreprocessor:
    """Preprocessor for legal text data."""

    def clean_text(self, text):
        """Normalize whitespace and strip leading/trailing whitespace.

        Args:
            text: Input text string.

        Returns:
            Cleaned text string.
        """
        text = re.sub(r"\s+", " ", text)
        text = text.strip()
        return text

    def truncate_text(self, text, max_length=512):
        """Truncate text to a maximum number of words.

        Args:
            text: Input text string.
            max_length: Maximum number of words.

        Returns:
            Truncated text string.
        """
        words = text.split()
        if len(words) > max_length:
            words = words[:max_length]
        return " ".join(words)

    def prepare_for_model(self, texts, tokenizer, max_length=512):
        """Tokenize a batch of texts for model input.

        Args:
            texts: List of text strings.
            tokenizer: HuggingFace tokenizer instance.
            max_length: Maximum token length.

        Returns:
            Tokenized batch (dict with input_ids, attention_mask, etc.).
        """
        return tokenizer(
            texts,
            max_length=max_length,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )
