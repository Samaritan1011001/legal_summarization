"""Evaluation module for summarization quality using ROUGE scores."""

from __future__ import annotations

from typing import Dict, List, Optional

from rouge_score import rouge_scorer


def calculate_rouge(reference: str, hypothesis: str) -> Dict[str, Dict[str, float]]:
    """Calculate ROUGE scores between reference and hypothesis summaries.
    
    Args:
        reference: The reference (ground truth) summary.
        hypothesis: The generated summary to evaluate.
        
    Returns:
        Dictionary with ROUGE-1, ROUGE-2, and ROUGE-L scores,
        each containing precision, recall, and fmeasure.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    
    result = {}
    for metric, score in scores.items():
        result[metric] = {
            "precision": score.precision,
            "recall": score.recall,
            "fmeasure": score.fmeasure,
        }
    
    return result


def evaluate_dataset(
    documents: list[dict],
    summarize_fn,
    num_sentences: int = 3,
    max_samples: Optional[int] = None,
) -> dict:
    """Evaluate summarization on a dataset.
    
    Args:
        documents: List of document dictionaries with original_text and reference_summary.
        summarize_fn: Function that takes text and returns a summary.
        num_sentences: Number of sentences for the summarizer.
        max_samples: Maximum number of samples to evaluate. None for all.
        
    Returns:
        Dictionary with average ROUGE scores and individual results.
    """
    if max_samples is not None:
        documents = documents[:max_samples]
    
    all_scores = []
    
    for doc in documents:
        original = doc.get("original_text", "")
        reference = doc.get("reference_summary", "")
        
        if not original or not reference:
            continue
        
        hypothesis = summarize_fn(original, num_sentences=num_sentences)
        scores = calculate_rouge(reference, hypothesis)
        all_scores.append({
            "uid": doc.get("uid", ""),
            "scores": scores,
        })
    
    # Calculate averages
    if not all_scores:
        return {"average": {}, "individual": []}
    
    avg_scores = {
        "rouge1": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
        "rouge2": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
        "rougeL": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
    }
    
    n = len(all_scores)
    for result in all_scores:
        for metric in avg_scores:
            for measure in ["precision", "recall", "fmeasure"]:
                avg_scores[metric][measure] += result["scores"][metric][measure]
    
    for metric in avg_scores:
        for measure in ["precision", "recall", "fmeasure"]:
            avg_scores[metric][measure] /= n
    
    return {
        "average": avg_scores,
        "num_samples": n,
        "individual": all_scores,
    }
