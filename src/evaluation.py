"""Evaluation utilities for summarization quality assessment."""

from rouge_score import rouge_scorer


class SummarizationEvaluator:
    """Evaluator for summarization quality using ROUGE metrics."""

    def __init__(self):
        self.scorer = rouge_scorer.RougeScorer(
            ["rouge1", "rouge2", "rougeL"], use_stemmer=True
        )

    def compute_rouge(self, predictions, references):
        """Compute ROUGE scores between predictions and references.

        Args:
            predictions: List of predicted summary strings.
            references: List of reference summary strings.

        Returns:
            Dict with rouge1, rouge2, rougeL keys, each containing
            precision, recall, fmeasure.
        """
        rouge1_scores = []
        rouge2_scores = []
        rougeL_scores = []

        for pred, ref in zip(predictions, references):
            scores = self.scorer.score(ref, pred)
            rouge1_scores.append(scores["rouge1"])
            rouge2_scores.append(scores["rouge2"])
            rougeL_scores.append(scores["rougeL"])

        def avg_score(score_list):
            n = len(score_list)
            return {
                "precision": sum(s.precision for s in score_list) / n,
                "recall": sum(s.recall for s in score_list) / n,
                "fmeasure": sum(s.fmeasure for s in score_list) / n,
            }

        return {
            "rouge1": avg_score(rouge1_scores),
            "rouge2": avg_score(rouge2_scores),
            "rougeL": avg_score(rougeL_scores),
        }

    def compute_statistics(self, predictions, references):
        """Compute length statistics for predictions and references.

        Args:
            predictions: List of predicted summary strings.
            references: List of reference summary strings.

        Returns:
            Dict with avg_prediction_length, avg_reference_length, compression_ratio.
        """
        pred_lengths = [len(p.split()) for p in predictions]
        ref_lengths = [len(r.split()) for r in references]

        avg_pred = sum(pred_lengths) / len(pred_lengths) if pred_lengths else 0
        avg_ref = sum(ref_lengths) / len(ref_lengths) if ref_lengths else 0

        compression_ratio = avg_pred / avg_ref if avg_ref > 0 else 0

        return {
            "avg_prediction_length": avg_pred,
            "avg_reference_length": avg_ref,
            "compression_ratio": compression_ratio,
        }

    def evaluate(self, predictions, references):
        """Run full evaluation: ROUGE scores and statistics.

        Args:
            predictions: List of predicted summary strings.
            references: List of reference summary strings.

        Returns:
            Dict with rouge_scores and statistics.
        """
        return {
            "rouge_scores": self.compute_rouge(predictions, references),
            "statistics": self.compute_statistics(predictions, references),
        }
