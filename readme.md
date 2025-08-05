# ESPN Fantasy Football Data Pipeline

This project builds a historical dataset from my ESPN Fantasy Football league (2012–2024) by scraping data using the `espn-api` Python package, exporting it to CSV, and preparing it for analysis in Jupyter and visualization in Tableau.

---

## 📁 Project Structure

```
fantasy-football-project/
├── data/
│   └── analysis.ipynb            # Notebook for data exploration and visualization
│
├── scripts/
│   ├── get_matchups.py           # Scrapes weekly matchup data per season
│   ├── get_standings.py          # Scrapes team-level standings per season
│   └── get_season_summary.py     # Generates season summary metrics from CSVs
│
├── csvs/
│   ├── matchups/                 # Contains one CSV per season of weekly matchups
│   └── season/                   # Final standings + summary for each season
│
├── .env                          # Stores ESPN S2 + SWID cookies (not tracked in Git)
├── .gitignore                    # Ignores CSVs, secrets, and system files
└── README.md
```

---

## 🧠 Overview

This repo automates the process of:

1. Scraping ESPN fantasy football data using `espn-api`
2. Storing structured data as CSVs (matchups, standings, summaries)
3. Preparing clean inputs for data analysis and visualization

---

## 🔄 Workflow

1. **Run scraping scripts:**

   ```bash
   python scripts/get_matchups.py
   python scripts/get_standings.py
   python scripts/get_season_summary.py
   ```

2. **Explore data in notebook:**

   ```python
   # Load and analyze matchups or standings
   pd.read_csv("csvs/matchups/matchups_2024.csv")
   pd.read_csv("csvs/season/all_team_standings.csv")
   ```

3. **Export cleaned and organized data to a SQL database.**

4. **Visualize insights in Jupyter or Tableau.**

---

## 💠 Dependencies

- Python 3.9+
- [`espn-api`](https://github.com/cwendt94/espn-api)
- `pandas`
- `python-dotenv`

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🔒 Notes

- Requires a `.env` file with ESPN credentials:

  ```
  ESPN_S2=your_espn_s2_token
  SWID=your_swid_token
  ```

- Matchup and standings data is not tracked in Git (`csvs/` is ignored)

---

## 📊 Future Improvements

- Normalize team names and owners over time
- Integrate player-level stats and draft data
- Upload to SQL database for more advanced querying
- Build Tableau dashboards or interactive dashboards in Python

---

## ✍️ Author

Julian Bombard\
@jpbombard



