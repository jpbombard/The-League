from espn_api.football import League
from dotenv import load_dotenv
import os
import pandas as pd
import time

# Load credentials
load_dotenv()
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

# Config
LEAGUE_ID = 48346
START_YEAR = 2012
END_YEAR = 2024
OUTPUT_FILE = "csvs/season/all_team_standings.csv"

# Storage list
all_standings = []

for year in range(START_YEAR, END_YEAR + 1):
    try:
        print(f"📅 Getting standings for season {year}")
        league = League(
            league_id=LEAGUE_ID,
            year=year,
            espn_s2=espn_s2,
            swid=swid
        )

        for team in league.standings():
            all_standings.append({
                "Season": year,
                "Team ID": team.team_id,
                "Team Name": team.team_name,
                "Owner(s)": ", ".join(
                    f"{owner['firstName']} {owner['lastName']}"
                    for owner in team.owners
                ),
                "Wins": team.wins,
                "Losses": team.losses,
                "Points For": team.points_for,
                "Points Against": team.points_against,
                "Regular Season Rank": team.standing,
                "Final Rank": team.final_standing
            })

        time.sleep(1)

    except Exception as e:
        print(f"❌ Failed to get standings for {year}: {e}")

# Convert to DataFrame and export
df = pd.DataFrame(all_standings)
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Saved: {OUTPUT_FILE}")
