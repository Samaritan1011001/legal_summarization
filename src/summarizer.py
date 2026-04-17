"""Extractive summarization using TF-IDF sentence scoring."""

import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    """Tokenize text into words.
    
    Args:
        text: Input text to tokenize.
        
    Returns:
        List of lowercase word tokens.
    """
    # Simple tokenization: split on non-alphanumeric characters
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words


def split_sentences(text: str) -> list[str]:
    """Split text into sentences.
    
    Args:
        text: Input text to split.
        
    Returns:
        List of sentences.
    """
    # Split on sentence-ending punctuation followed by space or end
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Filter out empty sentences
    return [s.strip() for s in sentences if s.strip()]


def compute_tf(words: list[str]) -> dict[str, float]:
    """Compute term frequency for a list of words.
    
    Args:
        words: List of word tokens.
        
    Returns:
        Dictionary mapping words to their term frequency.
    """
    word_counts = Counter(words)
    total_words = len(words)
    if total_words == 0:
        return {}
    return {word: count / total_words for word, count in word_counts.items()}


def compute_idf(documents: list[list[str]]) -> dict[str, float]:
    """Compute inverse document frequency across documents.
    
    Args:
        documents: List of tokenized documents (each is a list of words).
        
    Returns:
        Dictionary mapping words to their IDF score.
    """
    num_docs = len(documents)
    if num_docs == 0:
        return {}
    
    # Count documents containing each word
    doc_freq = Counter()
    for doc in documents:
        unique_words = set(doc)
        doc_freq.update(unique_words)
    
    # Compute IDF with smoothing
    idf = {}
    for word, freq in doc_freq.items():
        idf[word] = math.log((num_docs + 1) / (freq + 1)) + 1
    
    return idf


def score_sentence(sentence: str, idf: dict[str, float]) -> float:
    """Score a sentence using TF-IDF.
    
    Args:
        sentence: The sentence to score.
        idf: IDF scores for words.
        
    Returns:
        TF-IDF score for the sentence.
    """
    words = tokenize(sentence)
    if not words:
        return 0.0
    
    tf = compute_tf(words)
    score = sum(tf.get(word, 0) * idf.get(word, 1) for word in words)
    return score


def summarize(text: str, num_sentences: int = 3, min_sentence_length: int = 10) -> str:
    """Generate an extractive summary using TF-IDF sentence scoring.
    
    Args:
        text: Input text to summarize.
        num_sentences: Number of sentences to include in summary.
        min_sentence_length: Minimum character length for a sentence to be considered.
        
    Returns:
        Extractive summary as a string.
    """
    sentences = split_sentences(text)
    
    # Filter short sentences
    valid_sentences = [s for s in sentences if len(s) >= min_sentence_length]
    
    if not valid_sentences:
        # Fall back to original sentences if all are too short
        valid_sentences = sentences if sentences else [text]
    
    if len(valid_sentences) <= num_sentences:
        return " ".join(valid_sentences)
    
    # Tokenize each sentence as a "document" for IDF calculation
    tokenized_sentences = [tokenize(s) for s in valid_sentences]
    
    # Compute IDF across all sentences
    idf = compute_idf(tokenized_sentences)
    
    # Score each sentence
    sentence_scores = []
    for i, sentence in enumerate(valid_sentences):
        score = score_sentence(sentence, idf)
        sentence_scores.append((i, sentence, score))
    
    # Sort by score (descending) and take top sentences
    sentence_scores.sort(key=lambda x: x[2], reverse=True)
    top_sentences = sentence_scores[:num_sentences]
    
    # Sort by original position to maintain coherence
    top_sentences.sort(key=lambda x: x[0])
    
    # Join sentences
    summary = " ".join(s[1] for s in top_sentences)
    return summary
