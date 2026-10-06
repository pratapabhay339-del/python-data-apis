# Python Data & APIs — Analysis Report

## Dataset overview

- Records: **15**
- Columns: **8**
- Average midterm score: **72.53**
- Average final score: **79.33**
- Pass rate: **100.0%**
- Top student: **Isha**

## Branch summary

| branch   |   students |   average_final_score |   average_attendance |   average_study_hours |
|:---------|-----------:|----------------------:|---------------------:|----------------------:|
| AI       |          4 |                 81.75 |                88.25 |                  5.75 |
| CSE      |          7 |                 83.57 |                89.57 |                  5.86 |
| IT       |          4 |                 69.5  |                79.5  |                  3.75 |

## Visualizations

- `final_score_distribution.png`
- `average_score_by_branch.png`
- `correlation_heatmap.png`

## REST API preview

The project successfully consumed a JSON REST endpoint and converted the response to a DataFrame.

|   student_id | name   | branch   |
|-------------:|:-------|:---------|
|         1001 | Aarav  | CSE      |
|         1002 | Diya   | CSE      |
|         1003 | Rohan  | IT       |
|         1004 | Ananya | CSE      |
|         1005 | Kabir  | AI       |

## Conclusion

The workflow demonstrates the complete data lifecycle: loading, cleaning, analysis, visualization, API consumption, JSON processing, and automated report generation.
