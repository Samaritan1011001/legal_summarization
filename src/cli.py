"""Command-line interface for legal text summarization."""

import click
from pathlib import Path

from .data_loader import load_dataset, get_sample
from .summarizer import summarize
from .evaluator import evaluate_dataset, calculate_rouge


@click.group()
def cli():
    """Legal text summarization CLI."""
    pass


@cli.command(name="summarize")
@click.option("--sample", is_flag=True, help="Summarize a random sample from the dataset")
@click.option("--text", type=str, help="Text to summarize")
@click.option("--sentences", "-n", default=3, help="Number of sentences in summary")
@click.option("--dataset", type=str, default="all_v1.json", help="Dataset file to use for --sample")
def summarize_cmd(sample: bool, text: str, sentences: int, dataset: str):
    """Summarize legal text.
    
    Use --sample to summarize a random document from the dataset,
    or --text to summarize custom input text.
    """
    if sample and text:
        click.echo("Error: Cannot use both --sample and --text", err=True)
        raise SystemExit(1)
    
    if not sample and not text:
        click.echo("Error: Must specify either --sample or --text", err=True)
        raise SystemExit(1)
    
    if sample:
        # Find dataset file
        data_dir = Path(__file__).parent.parent
        dataset_path = data_dir / dataset
        
        if not dataset_path.exists():
            click.echo(f"Error: Dataset file not found: {dataset_path}", err=True)
            raise SystemExit(1)
        
        docs = load_dataset(dataset_path)
        doc = get_sample(docs)
        
        click.echo("=" * 60)
        click.echo(f"Document: {doc.get('doc', 'Unknown')}")
        if doc.get('title'):
            click.echo(f"Title: {doc['title']}")
        click.echo("=" * 60)
        click.echo("\nOriginal Text:")
        click.echo("-" * 40)
        click.echo(doc["original_text"])
        click.echo("\n" + "-" * 40)
        click.echo("\nGenerated Summary:")
        click.echo("-" * 40)
        summary = summarize(doc["original_text"], num_sentences=sentences)
        click.echo(summary)
        
        if doc.get("reference_summary"):
            click.echo("\n" + "-" * 40)
            click.echo("\nReference Summary:")
            click.echo("-" * 40)
            click.echo(doc["reference_summary"])
            
            # Show ROUGE scores
            scores = calculate_rouge(doc["reference_summary"], summary)
            click.echo("\n" + "-" * 40)
            click.echo("\nROUGE Scores:")
            for metric, values in scores.items():
                click.echo(f"  {metric}: F1={values['fmeasure']:.4f}")
    else:
        summary = summarize(text, num_sentences=sentences)
        click.echo("\nGenerated Summary:")
        click.echo("-" * 40)
        click.echo(summary)


@cli.command()
@click.option("--dataset", type=str, default="all_v1.json", help="Dataset file to evaluate")
@click.option("--max-samples", "-n", type=int, default=None, help="Maximum samples to evaluate")
@click.option("--sentences", "-s", default=3, help="Number of sentences in summary")
def evaluate(dataset: str, max_samples: int, sentences: int):
    """Evaluate summarization quality using ROUGE scores."""
    data_dir = Path(__file__).parent.parent
    dataset_path = data_dir / dataset
    
    if not dataset_path.exists():
        click.echo(f"Error: Dataset file not found: {dataset_path}", err=True)
        raise SystemExit(1)
    
    click.echo(f"Loading dataset: {dataset}")
    docs = load_dataset(dataset_path)
    click.echo(f"Loaded {len(docs)} documents")
    
    if max_samples:
        click.echo(f"Evaluating on {max_samples} samples...")
    else:
        click.echo("Evaluating on all samples...")
    
    results = evaluate_dataset(
        docs,
        summarize,
        num_sentences=sentences,
        max_samples=max_samples,
    )
    
    click.echo("\n" + "=" * 60)
    click.echo("EVALUATION RESULTS")
    click.echo("=" * 60)
    click.echo(f"Samples evaluated: {results['num_samples']}")
    click.echo("\nAverage ROUGE Scores:")
    click.echo("-" * 40)
    
    for metric in ["rouge1", "rouge2", "rougeL"]:
        scores = results["average"][metric]
        click.echo(f"  {metric}:")
        click.echo(f"    Precision: {scores['precision']:.4f}")
        click.echo(f"    Recall:    {scores['recall']:.4f}")
        click.echo(f"    F1:        {scores['fmeasure']:.4f}")


if __name__ == "__main__":
    cli()
