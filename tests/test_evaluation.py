"""Tests for the evaluation module."""

import pytest

from src.evaluation import SummarizationEvaluator


@pytest.fixture
def evaluator():
    return SummarizationEvaluator()


class TestComputeRouge:
    def test_returns_expected_keys(self, evaluator, sample_predictions_and_references):
        predictions, references = sample_predictions_and_references
        scores = evaluator.compute_rouge(predictions, references)
        assert "rouge1" in scores
        assert "rouge2" in scores
        assert "rougeL" in scores

    def test_rouge_has_precision_recall_fmeasure(self, evaluator, sample_predictions_and_references):
        predictions, references = sample_predictions_and_references
        scores = evaluator.compute_rouge(predictions, references)
        for metric in ["rouge1", "rouge2", "rougeL"]:
            assert "precision" in scores[metric]
            assert "recall" in scores[metric]
            assert "fmeasure" in scores[metric]

    def test_perfect_scores_with_identical_texts(self, evaluator):
        texts = ["the quick brown fox", "jumps over the lazy dog"]
        scores = evaluator.compute_rouge(texts, texts)
        for metric in ["rouge1", "rouge2", "rougeL"]:
            assert scores[metric]["precision"] == pytest.approx(1.0)
            assert scores[metric]["recall"] == pytest.approx(1.0)
            assert scores[metric]["fmeasure"] == pytest.approx(1.0)

    def test_scores_between_zero_and_one(self, evaluator, sample_predictions_and_references):
        predictions, references = sample_predictions_and_references
        scores = evaluator.compute_rouge(predictions, references)
        for metric in ["rouge1", "rouge2", "rougeL"]:
            for key in ["precision", "recall", "fmeasure"]:
                assert 0.0 <= scores[metric][key] <= 1.0

    def test_empty_inputs_returns_zeros(self, evaluator):
        scores = evaluator.compute_rouge([], [])
        for metric in ["rouge1", "rouge2", "rougeL"]:
            assert scores[metric]["precision"] == 0.0
            assert scores[metric]["recall"] == 0.0
            assert scores[metric]["fmeasure"] == 0.0


class TestComputeStatistics:
    def test_returns_expected_keys(self, evaluator, sample_predictions_and_references):
        predictions, references = sample_predictions_and_references
        stats = evaluator.compute_statistics(predictions, references)
        assert "avg_prediction_length" in stats
        assert "avg_reference_length" in stats
        assert "compression_ratio" in stats

    def test_correct_avg_lengths(self, evaluator):
        predictions = ["one two three", "four five six"]
        references = ["a b", "c d"]
        stats = evaluator.compute_statistics(predictions, references)
        assert stats["avg_prediction_length"] == 3.0
        assert stats["avg_reference_length"] == 2.0

    def test_compression_ratio(self, evaluator):
        predictions = ["one two three", "four five six"]
        references = ["a b", "c d"]
        stats = evaluator.compute_statistics(predictions, references)
        assert stats["compression_ratio"] == pytest.approx(1.5)


class TestEvaluate:
    def test_returns_rouge_scores_and_statistics(self, evaluator, sample_predictions_and_references):
        predictions, references = sample_predictions_and_references
        results = evaluator.evaluate(predictions, references)
        assert "rouge_scores" in results
        assert "statistics" in results
        assert "rouge1" in results["rouge_scores"]
        assert "avg_prediction_length" in results["statistics"]

    def test_evaluate_empty_inputs(self, evaluator):
        results = evaluator.evaluate([], [])
        assert results["rouge_scores"]["rouge1"]["fmeasure"] == 0.0
        assert results["statistics"]["avg_prediction_length"] == 0
        assert results["statistics"]["avg_reference_length"] == 0
