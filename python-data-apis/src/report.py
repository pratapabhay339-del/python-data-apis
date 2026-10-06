"""Charts and Markdown report generation."""

from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_charts(df: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """Create analysis charts and return their paths."""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    plt.figure(figsize=(8, 5))
    plt.hist(df["final_score"], bins=6)
    plt.title("Distribution of Final Scores")
    plt.xlabel("Final Score")
    plt.tight_layout()
    path = output / "final_score_distribution.png"
    plt.savefig(path, dpi=150)
    plt.close()
    paths.append(path)

    branch_scores = df.groupby("branch")["final_score"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    branch_scores.plot(kind="bar")
    plt.title("Average Final Score by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Average Final Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    path = output / "average_score_by_branch.png"
    plt.savefig(path, dpi=150)
    plt.close()
    paths.append(path)

    plt.figure(figsize=(7, 5))
    sns.heatmap(df.select_dtypes("number").corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Numeric Feature Correlation")
    plt.tight_layout()
    path = output / "correlation_heatmap.png"
    plt.savefig(path, dpi=150)
    plt.close()
    paths.append(path)

    return paths


def generate_markdown_report(
    metrics: Dict[str, object], api_preview: pd.DataFrame, output_path: str | Path
) -> Path:
    """Generate a human-readable Markdown report."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    branch_summary: pd.DataFrame = metrics["branch_summary"]

    report = f"""# Python Data & APIs — Analysis Report

## Dataset overview

- Records: **{metrics['rows']}**
- Columns: **{metrics['columns']}**
- Average midterm score: **{metrics['average_midterm_score']}**
- Average final score: **{metrics['average_final_score']}**
- Pass rate: **{metrics['pass_rate']}%**
- Top student: **{metrics['top_student']}**

## Branch summary

{branch_summary.to_markdown(index=False)}

## Visualizations

- `final_score_distribution.png`
- `average_score_by_branch.png`
- `correlation_heatmap.png`

## REST API preview

The project successfully consumed a JSON REST endpoint and converted the response to a DataFrame.

{api_preview.to_markdown(index=False)}

## Conclusion

The workflow demonstrates the complete data lifecycle: loading, cleaning, analysis, visualization, API consumption, JSON processing, and automated report generation.
"""
    output.write_text(report, encoding="utf-8")
    return output
