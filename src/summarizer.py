"""Summarization model wrapper for legal text summarization."""

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class LegalSummarizer:
    """Wrapper around a HuggingFace seq2seq model for summarization."""

    def __init__(self, model_name="facebook/bart-large-cnn", device=None):
        """Initialize the summarizer with a pretrained model.

        Args:
            model_name: HuggingFace model name or path.
            device: Device to use ('cpu', 'cuda', etc.). Auto-detected if None.
        """
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def summarize(self, text, max_length=150, min_length=30):
        """Generate a summary for a single text.

        Args:
            text: Input text string.
            max_length: Maximum summary length in tokens.
            min_length: Minimum summary length in tokens.

        Returns:
            Summary string.
        """
        inputs = self.tokenizer(
            text, max_length=1024, truncation=True, return_tensors="pt"
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            summary_ids = self.model.generate(
                **inputs,
                max_length=max_length,
                min_length=min_length,
                num_beams=4,
                early_stopping=True,
            )

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    def summarize_batch(self, texts, max_length=150, min_length=30, batch_size=4):
        """Generate summaries for a batch of texts.

        Args:
            texts: List of input text strings.
            max_length: Maximum summary length in tokens.
            min_length: Minimum summary length in tokens.
            batch_size: Number of texts to process at once.

        Returns:
            List of summary strings.
        """
        summaries = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            inputs = self.tokenizer(
                batch,
                max_length=1024,
                truncation=True,
                padding=True,
                return_tensors="pt",
            )
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            with torch.no_grad():
                summary_ids = self.model.generate(
                    **inputs,
                    max_length=max_length,
                    min_length=min_length,
                    num_beams=4,
                    early_stopping=True,
                )

            batch_summaries = self.tokenizer.batch_decode(
                summary_ids, skip_special_tokens=True
            )
            summaries.extend(batch_summaries)

        return summaries
