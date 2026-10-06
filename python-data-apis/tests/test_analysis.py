import pandas as pd

from src.analysis import analyze_dataset, clean_dataset


def test_clean_dataset_removes_duplicates_and_fills_missing_values():
    raw = pd.DataFrame(
        {
            "student_id": [1, 1, 2],
            "name": [" A ", " A ", "B"],
            "branch": ["cse", "cse", "it"],
            "attendance_percent": [90, 90, None],
            "study_hours": [5, 5, 4],
            "assignments_completed": [8, 8, 7],
            "midterm_score": [70, 70, 60],
            "final_score": [80, 80, 65],
        }
    )
    cleaned = clean_dataset(raw)
    assert len(cleaned) == 2
    assert cleaned["attendance_percent"].isna().sum() == 0
    assert cleaned.loc[0, "name"] == "A"
    assert cleaned.loc[0, "branch"] == "CSE"


def test_analyze_dataset_returns_expected_metrics():
    df = pd.DataFrame(
        {
            "student_id": [1, 2],
            "name": ["A", "B"],
            "branch": ["CSE", "IT"],
            "attendance_percent": [90, 80],
            "study_hours": [5, 4],
            "assignments_completed": [8, 7],
            "midterm_score": [70, 60],
            "final_score": [80, 60],
        }
    )
    result = analyze_dataset(df)
    assert result["rows"] == 2
    assert result["average_final_score"] == 70.0
    assert result["pass_rate"] == 100.0
    assert result["top_student"] == "A"
