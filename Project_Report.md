# Project Report: Global Olympic Sports Performance Analysis

## 1. Abstract
This project explores historical Olympic athlete-event records to understand medal patterns across time, National Olympic Committee (NOC) codes, and sports. Tableau is used to build an interactive dashboard, while Python and Flask provide a small web-based companion for filtering and reviewing results.

## 2. Problem statement
Olympic datasets contain many records across different years, sports, countries, and medal types. A visual analysis can make these patterns easier to compare and communicate.

## 3. Objectives
- Examine medal-winning athlete records across Olympic years.
- Identify the NOCs with the largest medal-winning record counts.
- Compare Gold, Silver, and Bronze records.
- Explore which sports have high medal-winning record counts.
- Present findings in Tableau and a simple Flask web app.

## 4. Dataset
The project uses `athlete_events.csv` and optionally `noc_regions.csv` from the downloaded Olympic athlete-events dataset. Record the source URL, download date, and dataset license here before final submission.

**Coverage note:** The commonly used version covers 1896–2016. Verify the years in your actual file.

## 5. Methodology
1. Load the CSV data with pandas.
2. Check field names and missing medal values.
3. Filter medal records to Gold, Silver, and Bronze.
4. Group records by year, NOC, medal type, and sport.
5. Visualize results in Tableau and present summary tables in Flask.
6. Compare outputs and note limitations.

## 6. Visualizations
- **Medal Trends Over Time:** year on the horizontal axis, record count on the vertical axis, medal type as color.
- **Top 10 Olympic Countries:** NOC codes ranked by medal-winning athlete record count.
- **Medals by Type:** counts for Gold, Silver, and Bronze.
- **Dashboard filters:** season and year where appropriate.

## 7. Findings
Fill this section after running the analysis. Use actual results from your workbook; do not copy assumptions.

- Highest NOC by medal-winning athlete records: [add result]
- Most represented medal type: [add result]
- Trend or change across years: [add result]
- Sport with the highest record count: [add result]
- One additional observation: [add result]

## 8. Limitations
- A row represents an athlete-event record, not necessarily a unique physical medal.
- Team events can produce multiple athlete records for the same medal.
- NOC codes and historical country boundaries may change over time.
- Missing values and historical differences in event programs can affect comparisons.
- Results depend on the exact dataset version used.

## 9. Conclusion
Summarize the most important verified patterns from your own analysis. Explain how Tableau and Flask help viewers explore the data.

## 10. Future improvements
- Deduplicate team medals using a documented method if unique medal counts are required.
- Add athlete-level filters and sport-specific comparisons.
- Improve accessibility and add downloadable filtered summaries.
- Deploy the web app only after checking hosting, security, and dataset-license requirements.

## 11. References
- Dataset: [insert exact Kaggle dataset URL and creator]
- Tableau Public: https://public.tableau.com/
- Flask documentation: https://flask.palletsprojects.com/
- pandas documentation: https://pandas.pydata.org/docs/
