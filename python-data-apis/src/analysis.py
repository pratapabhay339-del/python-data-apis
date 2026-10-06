"""Data loading, cleaning, and analysis utilities."""

from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd

NUMERIC_COLUMNS = [
    "attendance_percent",
    "study_hours",
    "assignments_completed",
    "midterm_score",
    "final_score",
]


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the CSV dataset into a DataFrame."""
    return pd.read_csv(path)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy with normalized types and filled missing values."""
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip().str.lower()

    for column in NUMERIC_COLUMNS:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
        if cleaned[column].isna().any():
            cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    cleaned["name"] = cleaned["name"].astype(str).str.strip()
    cleaned["branch"] = cleaned["branch"].astype(str).str.strip().str.upper()
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    return cleaned


def analyze_dataset(df: pd.DataFrame) -> Dict[str, object]:
    """Calculate useful summary metrics for the cleaned dataset."""
    average_final = float(np.mean(df["final_score"]))
    average_midterm = float(np.mean(df["midterm_score"]))
    pass_rate = float((df["final_score"] >= 40).mean() * 100)

    branch_summary = (
        df.groupby("branch", as_index=False)
        .agg(
            students=("student_id", "count"),
            average_final_score=("final_score", "mean"),
            average_attendance=("attendance_percent", "mean"),
            average_study_hours=("study_hours", "mean"),
        )
        .round(2)
    )

    top_student = df.loc[df["final_score"].idxmax(), "name"]

    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "average_final_score": round(average_final, 2),
        "average_midterm_score": round(average_midterm, 2),
        "pass_rate": round(pass_rate, 2),
        "top_student": str(top_student),
        "branch_summary": branch_summary,
    }


def clean_and_analyze(path: str | Path) -> Tuple[pd.DataFrame, Dict[str, object]]:
    """Load, clean, and analyze a dataset in one call."""
    return (lambda raw: (clean_dataset(raw), analyze_dataset(clean_dataset(raw))))(
        load_dataset(path)
    )
