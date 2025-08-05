import os
import pandas as pd
import glob

# File paths
MATCHUP_DIR = "csvs/matchups"
STANDINGS_FILE = "csvs/season/all_team_standings.csv"
SUMMARY_FILE = "csvs/season/season_summaries.csv"

# Load standings
df_standings = pd.read_csv(STANDINGS_FILE)

# Collect all matchup files
matchup_files = sorted(glob.glob(f"{MATCHUP_DIR}/matchups_*.csv"))

# List to store summary rows
season_summaries = []

for file in matchup_files:
    # Extract year from file name
    year = int(os.path.basename(file).split("_")[1].split(".")[0])
    
    # Load matchups for the season
    df = pd.read_csv(file)

    # Calculate summary stats
    avg_score = df["Score"].mean()
    num_teams = df["Team ID"].nunique()
    total_points = df.groupby("Team ID")["Score"].sum()
    highest_total_team_id = total_points.idxmax()

    # Champion and runner-up from standings
    standings_this_season = df_standings[df_standings["Season"] == year]

    champion = standings_this_season[standings_this_season["Final Rank"] == 1]
    runner_up = standings_this_season[standings_this_season["Final Rank"] == 2]

    season_summaries.append({
        "Season": year,
        "Num Teams": num_teams,
        "Champion Team ID": champion["Team ID"].values[0] if not champion.empty else None,
        "Runner-Up Team ID": runner_up["Team ID"].values[0] if not runner_up.empty else None,
        "Highest Total Points Team ID": highest_total_team_id,
        "Average Weekly Score": round(avg_score, 2)
    })

# Create DataFrame and export
df_summary = pd.DataFrame(season_summaries)
os.makedirs(os.path.dirname(SUMMARY_FILE), exist_ok=True)
df_summary.to_csv(SUMMARY_FILE, index=False)

print(f"✅ Saved: {SUMMARY_FILE}")
