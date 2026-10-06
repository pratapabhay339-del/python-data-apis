"""Run the complete Module 4 data + API workflow."""

from pathlib import Path

from .analysis import clean_and_analyze
from .api_client import get_api_preview
from .report import create_charts, generate_markdown_report

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "student_performance.csv"
REPORT_DIR = ROOT / "reports"


def main() -> None:
    print("=== Python Data & APIs | Module 4 ===")
    df, metrics = clean_and_analyze(DATASET)
    print(f"Loaded {metrics['rows']} records with {metrics['columns']} columns.")
    print(f"Average final score: {metrics['average_final_score']}")
    print(f"Pass rate: {metrics['pass_rate']}%")
    print(f"Top student: {metrics['top_student']}")

    chart_paths = create_charts(df, REPORT_DIR)
    print("Created charts:")
    for path in chart_paths:
        print(f"  - {path.relative_to(ROOT)}")

    try:
        api_preview = get_api_preview()
        print(f"REST API: fetched {len(api_preview)} preview records.")
    except Exception as exc:
        print(f"REST API unavailable right now: {exc}")
        # Keep report generation usable even if the public API is temporarily down.
        api_preview = df[["student_id", "name", "branch"]].head(5)

    report_path = generate_markdown_report(metrics, api_preview, REPORT_DIR / "analysis_report.md")
    print(f"Report generated: {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
