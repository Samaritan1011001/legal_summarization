"""Main pipeline for legal text summarization."""

import argparse
import json
import os

from src.data_loader import load_dataset, get_splits, get_statistics
from src.preprocessing import TextPreprocessor
from src.summarizer import LegalSummarizer
from src.evaluation import SummarizationEvaluator


def parse_args():
    parser = argparse.ArgumentParser(
        description="Legal text summarization pipeline"
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="all_v1.json",
        help="Path to the dataset JSON file",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="facebook/bart-large-cnn",
        help="HuggingFace model name for summarization",
    )
    parser.add_argument(
        "--max_samples",
        type=int,
        default=None,
        help="Maximum number of test samples to process (for quick testing)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="results/",
        help="Directory to save results",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=4,
        help="Batch size for summarization",
    )
    return parser.parse_args()


def run_pipeline(args):
    """Run the full summarization pipeline.

    Args:
        args: Parsed command-line arguments.
    """
    # Load data
    print(f"Loading dataset from {args.dataset}...")
    data = load_dataset(args.dataset)
    stats = get_statistics(data)
    print(f"Loaded {stats['record_count']} records")
    print(f"Avg original length: {stats['avg_original_length']:.1f} words")
    print(f"Avg summary length: {stats['avg_summary_length']:.1f} words")
    print(f"Sources: {stats['sources']}")

    # Split data
    splits = get_splits(data)
    print(
        f"Splits - Train: {len(splits['train'])}, "
        f"Val: {len(splits['val'])}, "
        f"Test: {len(splits['test'])}"
    )

    # Get test set
    test_data = splits["test"]
    if args.max_samples is not None:
        test_data = test_data[: args.max_samples]
    print(f"Processing {len(test_data)} test samples...")

    # Preprocess
    preprocessor = TextPreprocessor()
    texts = [preprocessor.clean_text(r["original_text"]) for r in test_data]
    references = [r["reference_summary"] for r in test_data]

    # Summarize
    print(f"Loading model: {args.model}...")
    summarizer = LegalSummarizer(model_name=args.model)

    print(f"Summarizing {len(texts)} texts in batches of {args.batch_size}...")
    predictions = summarizer.summarize_batch(
        texts, batch_size=args.batch_size
    )

    # Evaluate
    print("Evaluating...")
    evaluator = SummarizationEvaluator()
    results = evaluator.evaluate(predictions, references)

    # Print results
    print("\n--- Results ---")
    for metric, scores in results["rouge_scores"].items():
        print(
            f"{metric}: P={scores['precision']:.4f} "
            f"R={scores['recall']:.4f} "
            f"F={scores['fmeasure']:.4f}"
        )
    print(
        f"Avg prediction length: "
        f"{results['statistics']['avg_prediction_length']:.1f} words"
    )
    print(
        f"Avg reference length: "
        f"{results['statistics']['avg_reference_length']:.1f} words"
    )
    print(
        f"Compression ratio: "
        f"{results['statistics']['compression_ratio']:.2f}"
    )

    # Save results
    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, "results.json")

    output_data = {
        "dataset": args.dataset,
        "model": args.model,
        "num_samples": len(test_data),
        "dataset_statistics": stats,
        "results": results,
        "predictions": [
            {
                "original": texts[i],
                "reference": references[i],
                "prediction": predictions[i],
            }
            for i in range(len(predictions))
        ],
    }

    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args)
