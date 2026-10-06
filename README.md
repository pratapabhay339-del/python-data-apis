# Python Data & APIs

A complete Module 4 project covering **NumPy, Pandas, data cleaning, visualization, REST APIs, JSON processing, and automated report generation**.

## Module 4 — Python Data & APIs

### Learning outcomes
- Load and inspect datasets with Pandas and NumPy.
- Clean missing, duplicate, and inconsistent data.
- Perform descriptive analysis and aggregations.
- Create visualizations with Matplotlib and Seaborn.
- Consume a REST API using Python HTTP requests.
- Process JSON API responses.
- Generate a Markdown analysis report automatically.
- Run the complete workflow from one command.

## Project structure

```text
python-data-apis/
├── data/
│   └── student_performance.csv       # Sample dataset
├── notebooks/
│   └── module4_python_data_apis.ipynb # Google Colab-ready notebook
├── reports/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── analysis.py                   # Cleaning + analysis
│   ├── api_client.py                 # REST API + JSON processing
│   ├── report.py                     # Report generation
│   └── main.py                       # End-to-end application
├── tests/
│   └── test_analysis.py
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/python-data-apis.git
cd python-data-apis
python -m venv .venv
```

### Windows
```bash
.venv\Scripts\activate
```

### Linux/macOS
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

From the repository root:

```bash
python -m src.main
```

The application will:
1. Load the CSV dataset.
2. Clean duplicates and missing values.
3. Calculate summary statistics and performance metrics.
4. Create charts in `reports/`.
5. Call a public REST API and process its JSON response.
6. Generate `reports/analysis_report.md`.

## Run tests

```bash
pytest -q
```

## Google Colab

Upload `notebooks/module4_python_data_apis.ipynb` to Google Colab or open it directly from GitHub. The notebook is self-contained and demonstrates the same workflow interactively.

## REST API used

The project uses JSONPlaceholder's public `/posts` endpoint for a simple REST API demonstration. No API key is required.

## Academic coverage

| Requirement | Implementation |
|---|---|
| NumPy | Statistical calculations and arrays |
| Pandas | DataFrame loading, cleaning, grouping |
| Data cleaning | Missing values, duplicates, type normalization |
| Matplotlib | Performance and distribution charts |
| Seaborn | Correlation heatmap |
| REST API | HTTP GET request |
| JSON | Response parsing and tabular conversion |
| Data analysis app | `src/main.py` |
| Report generation | `src/report.py` |
| Testing | `tests/test_analysis.py` |

## Submission checklist

- [x] GitHub repository
- [x] Source code
- [x] Dataset
- [x] Google Colab-ready notebook
- [x] Requirements file
- [x] Automated report generation
- [x] API integration
- [x] Tests
- [x] README documentation
- [ ] LinkedIn post link — add after publishing

## Author

**Abhay Pratap Mall**  
B.Tech CSE
