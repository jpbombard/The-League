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
MAX_WEEKS = 17
OUTPUT_DIR = "csvs/matchups"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for year in range(START_YEAR, END_YEAR + 1):
    try:
        print(f"📅 Loading matchups for season {year}")
        league = League(
            league_id=LEAGUE_ID,
            year=year,
            espn_s2=espn_s2,
            swid=swid
        )

        season_matchups = []

        for week in range(1, MAX_WEEKS + 1):
            matchups = league.scoreboard(week=week)
            for matchup in matchups:
                home = getattr(matchup, "home_team", None)
                away = getattr(matchup, "away_team", None)


                # Skip completely empty matchups (very rare)
                if home is None and away is None:
                    continue

                # Regular matchup with both teams
                if home and away:
                    season_matchups.extend([
                        {
                            "Season": year,
                            "Week": week,
                            "Team ID": home.team_id,
                            "Team Name": home.team_name,
                            "Opponent ID": away.team_id,
                            "Opponent Name": away.team_name,
                            "Score": matchup.home_score,
                            "Opponent Score": matchup.away_score,
                            "Is Home": True,
                            "Is Winner": matchup.home_score > matchup.away_score,
                            "Is Playoff": getattr(matchup, "playoff", False),
                            "Is Consolation": getattr(matchup, "consolation", False),
                            "Is Bye Week": False
                        },
                        {
                            "Season": year,
                            "Week": week,
                            "Team ID": away.team_id,
                            "Team Name": away.team_name,
                            "Opponent ID": home.team_id,
                            "Opponent Name": home.team_name,
                            "Score": matchup.away_score,
                            "Opponent Score": matchup.home_score,
                            "Is Home": False,
                            "Is Winner": matchup.away_score > matchup.home_score,
                            "Is Playoff": getattr(matchup, "playoff", False),
                            "Is Consolation": getattr(matchup, "consolation", False),
                            "Is Bye Week": False
                        }
                    ])

                # Bye week for home team only
                elif home and not away:
                    season_matchups.append({
                        "Season": year,
                        "Week": week,
                        "Team ID": home.team_id,
                        "Team Name": home.team_name,
                        "Opponent ID": None,
                        "Opponent Name": "BYE",
                        "Score": matchup.home_score,
                        "Opponent Score": None,
                        "Is Home": True,
                        "Is Winner": None,
                        "Is Playoff": getattr(matchup, "playoff", False),
                        "Is Consolation": getattr(matchup, "consolation", False),
                        "Is Bye Week": True
                    })

                # Bye week for away team only (rare)
                elif away and not home:
                    season_matchups.append({
                        "Season": year,
                        "Week": week,
                        "Team ID": away.team_id,
                        "Team Name": away.team_name,
                        "Opponent ID": None,
                        "Opponent Name": "BYE",
                        "Score": matchup.away_score,
                        "Opponent Score": None,
                        "Is Home": False,
                        "Is Winner": None,
                        "Is Playoff": getattr(matchup, "playoff", False),
                        "Is Consolation": getattr(matchup, "consolation", False),
                        "Is Bye Week": True
                    })

        # Export CSV for the season
        df = pd.DataFrame(season_matchups)
        output_path = f"{OUTPUT_DIR}/matchups_{year}.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Saved: {output_path}")

        time.sleep(1)  # be kind to ESPN servers

    except Exception as e:
        print(f"❌ Failed for season {year}: {e}")
