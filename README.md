# Global Olympic Sports Performance Analysis

A student project that explores historical Olympic athlete and medal records using Python, Flask, and Tableau.

## Project features

- Medal record summary: Gold, Silver, Bronze
- Top 10 NOCs by medal-winning athlete records
- Medal trends by Olympic year and medal type
- Top sports by medal-winning athlete records
- Season and year filters in the Flask page
- Tableau dashboard companion

## Dataset setup

This project expects the Kaggle Olympic athlete-events dataset with these files:

- `athlete_events.csv`
- `noc_regions.csv`

Create a folder named `data` beside `app.py`, then place both CSV files inside it:

```text
Global_Olympic_Sports_Performance_Analysis/
├── app.py
├── analysis.py
├── requirements.txt
├── data/
│   ├── athlete_events.csv
│   └── noc_regions.csv
├── templates/
│   ├── index.html
│   └── setup.html
└── static/
    └── style.css
```

The CSVs are not included in this starter package. Use the dataset you already downloaded and check its license/attribution requirements.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

5. Put the two CSV files in `data/`.
6. Start the app:
   ```powershell
   python app.py
   ```
7. Open the local address shown in the terminal (normally `http://127.0.0.1:5000`).

## Tableau dashboard

Create a Tableau Public workbook with these worksheets:

1. **Medal Trends Over Time**: Year on Columns, count of records on Rows, Medal on Color, exclude Medal = Null. Add Season as a filter.
2. **Top 10 Olympic Countries**: NOC on Rows, count of ID/records on Columns, filter to Top 10 by count.
3. **Medals by Type**: Medal on Columns, count of ID/records on Rows, exclude Null medals.
4. **Olympic Medal Dashboard**: add all three worksheets, add a clear title, and show relevant filters.

Save your workbook as `Global_Olympic_Project.twbx` if you want to package local data extracts, or save it in Tableau Public according to your assignment instructions.

## Important interpretation note

The dataset contains one row per athlete-event participation, not necessarily one row per unique medal. Team events can create multiple athlete records for one medal. Therefore, counts in this app and starter Tableau charts are labelled as **medal-winning athlete records**, not unique physical medals. If the assignment requires unique medal counts, define and document a team-event deduplication method first.

The dataset commonly used for this project covers Olympic Games from 1896 through 2016. Do not describe it as including later Games unless your CSV contains them.

## Suggested project objectives

- Explore how medal-winning athlete records vary over time.
- Compare the countries/NOCs with the most medal-winning athlete records.
- Compare Gold, Silver, and Bronze record counts.
- Identify sports with high medal-winning athlete record counts.
- Present findings through an interactive Tableau dashboard and a simple web application.

## Suggested deliverables

- `Global_Olympic_Project.twbx` — Tableau workbook, created by you
- This Flask project folder
- `Project_Report.md` — report template
- `Presentation_Outline.md` — slide outline
- A short screen recording showing the dashboard and web app

## Data and privacy

Keep the raw dataset out of public Git repositories unless its license permits redistribution. This starter's `.gitignore` excludes CSVs under `data/`.
