"""Tests for summarizer module."""

import pytest

from src.summarizer import (
    tokenize,
    split_sentences,
    compute_tf,
    compute_idf,
    score_sentence,
    summarize,
)


class TestTokenize:
    """Tests for tokenize function."""
    
    def test_basic_tokenization(self):
        """Test basic word tokenization."""
        text = "Hello world, this is a test."
        tokens = tokenize(text)
        assert tokens == ["hello", "world", "this", "is", "a", "test"]
    
    def test_empty_text(self):
        """Test tokenization of empty text."""
        assert tokenize("") == []
    
    def test_lowercase(self):
        """Test that tokens are lowercased."""
        text = "HELLO World"
        tokens = tokenize(text)
        assert all(t.islower() for t in tokens)


class TestSplitSentences:
    """Tests for split_sentences function."""
    
    def test_basic_split(self):
        """Test basic sentence splitting."""
        text = "First sentence. Second sentence. Third sentence."
        sentences = split_sentences(text)
        assert len(sentences) == 3
    
    def test_single_sentence(self):
        """Test text with single sentence."""
        text = "This is a single sentence."
        sentences = split_sentences(text)
        assert len(sentences) == 1
    
    def test_empty_text(self):
        """Test splitting empty text."""
        assert split_sentences("") == []


class TestComputeTf:
    """Tests for compute_tf function."""
    
    def test_basic_tf(self):
        """Test basic term frequency calculation."""
        words = ["the", "cat", "sat", "on", "the", "mat"]
        tf = compute_tf(words)
        assert tf["the"] == 2 / 6
        assert tf["cat"] == 1 / 6
    
    def test_empty_words(self):
        """Test TF with empty word list."""
        assert compute_tf([]) == {}


class TestComputeIdf:
    """Tests for compute_idf function."""
    
    def test_basic_idf(self):
        """Test basic IDF calculation."""
        docs = [
            ["the", "cat"],
            ["the", "dog"],
            ["a", "bird"],
        ]
        idf = compute_idf(docs)
        # "the" appears in 2 docs, should have lower IDF than "cat"
        assert idf["the"] < idf["cat"]
    
    def test_empty_docs(self):
        """Test IDF with empty document list."""
        assert compute_idf([]) == {}


class TestScoreSentence:
    """Tests for score_sentence function."""
    
    def test_basic_scoring(self):
        """Test basic sentence scoring."""
        idf = {"important": 2.0, "word": 1.5, "the": 0.5}
        score = score_sentence("The important word", idf)
        assert score > 0
    
    def test_empty_sentence(self):
        """Test scoring empty sentence."""
        assert score_sentence("", {}) == 0.0


class TestSummarize:
    """Tests for summarize function."""
    
    def test_basic_summarization(self):
        """Test basic summarization."""
        text = (
            "This is the first sentence about legal terms. "
            "The second sentence discusses privacy policy. "
            "Third sentence covers user agreements. "
            "Fourth sentence mentions data protection. "
            "Fifth sentence talks about service terms."
        )
        summary = summarize(text, num_sentences=2)
        
        # Summary should be shorter than original
        assert len(summary) < len(text)
        # Summary should contain some content
        assert len(summary) > 0
    
    def test_short_text(self):
        """Test summarization of text shorter than requested sentences."""
        text = "Short text. Only two sentences."
        summary = summarize(text, num_sentences=5)
        
        # Should return all sentences when text is shorter
        assert "Short text" in summary
        assert "Only two sentences" in summary
    
    def test_empty_text(self):
        """Test summarization of empty text."""
        summary = summarize("", num_sentences=3)
        assert summary == ""
    
    def test_single_sentence(self):
        """Test summarization of single sentence."""
        text = "This is a single sentence about legal matters."
        summary = summarize(text, num_sentences=3)
        assert summary == text
    
    def test_legal_text(self):
        """Test summarization of legal-style text."""
        text = (
            "By using our services you agree to these terms. "
            "We may collect personal information as described in our privacy policy. "
            "You must be at least 18 years old to use this service. "
            "We reserve the right to modify these terms at any time. "
            "Your continued use constitutes acceptance of any changes."
        )
        summary = summarize(text, num_sentences=2)
        
        # Summary should contain complete sentences
        assert summary.endswith(".")
        # Summary should be non-empty
        assert len(summary) > 10
