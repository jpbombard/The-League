# ESPN Fantasy Football Data Pipeline

This project builds a historical dataset from my ESPN Fantasy Football league (2012–2024) by scraping data using the `espn-api` Python package, exporting it to CSV, cleaning and normalizing in notebooks, and finally loading into a SQLite database for analysis and visualization.

---

## Project Structure

```
fantasy-football-project/
├── data/
│   ├── analysis.ipynb             # Notebook for analysis and exploration
│   ├── cleaning.ipynb             # Notebook for data cleaning
│   └── export.ipynb               # Notebook for exporting cleaned data to database
│
├── scripts/
│   ├── get_matchups.py            # Scrapes weekly matchup data per season
│   ├── get_standings.py           # Scrapes team-level standings per season
│   └── get_season_summary.py      # Generates season summary metrics from CSVs
│
├── csvs/
│   ├── matchups/                  # Raw per-season matchup data
│   └── season/                    # Raw per-season standings and summaries
│
├── db/
│   ├── League_DB                  # SQLite database file
│   └── sql_scripts/               # SQL queries and scripts for analysis
│
├── .env                           # Stores ESPN S2 + SWID cookies (not tracked in Git)
├── .gitignore                     # Ignores raw CSVs, secrets, and system files
└── README.md
```

---

## Overview

This repo automates the end-to-end pipeline of fantasy football data:

1. **Scraping** ESPN fantasy football data with `espn-api`.
2. **Exporting raw CSVs** for matchups, standings, and summaries.
3. **Cleaning** the raw CSVs using `cleaning.ipynb`.
4. **Exporting** cleaned data from `export.ipynb` into a SQLite database.
5. **Analyzing data** in `analysis.ipynb` or with SQL in DBeaver.

---

## Workflow

1. **Run scraping scripts** to fetch raw data and save to `csvs/`:

   ```bash
   python scripts/get_matchups.py
   python scripts/get_standings.py
   python scripts/get_season_summary.py
   ```

2. **Clean raw data** in `cleaning.ipynb`.

   * Normalize owner names
   * Fix playoff/consolation flags
   * Generate cleaned CSVs (e.g., `matchups_all_cleaned.csv`)

3. **Export to database** in `export.ipynb`, loading the cleaned CSVs into `db/League_DB`.

4. **Explore data** in `analysis.ipynb` or run SQL queries directly from `db/sql_scripts/` in DBeaver.

---

## Dependencies

* Python 3.9+
* [`espn-api`](https://github.com/cwendt94/espn-api)
* `pandas`
* `python-dotenv`
* `sqlalchemy`

Install requirements:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* Build Tableau dashboards for visualization of league trends, playoff outcomes, and historical team performance.
* Perform statistical analyses such as regression, t-tests, or hypothesis testing on fantasy outcomes.
* Expand the dataset to include player-level statistics and draft data.
* Create advanced SQL views and analytical queries for richer insights.

---

## Author

Julian Bombard
@jpbombard
