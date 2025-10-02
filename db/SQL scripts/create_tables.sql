CREATE TABLE IF NOT EXISTS teams_season (
	Season Integer,
	Team_Id Integer, 
	Team_Name Varchar(255),
	Owners Varchar(255),
	Wins Integer,
	Losses Integer,
	Points_For Numeric,
	Points_Against Numeric,
	Regular_Season_Rank Integer,
	Final_Rank Integer
)

CREATE TABLE IF NOT EXISTS matchups_team (
	Season Integer,
	Week Integer,
	Team_Id Integer,
	Team_Name Varchar(255),
	Owners Varchar(255),
	Opponent_Id Integer,
	Opponent_Name Varchar(255),
	Score Numeric,
	Opponent_Score Numeric,
	Is_Home Boolean,
	Is_Bye_Week Boolean,
	Is_Playoff Boolean,
	Is_Consolation Boolean,
	Foreign Key (Team_Id) References teams_season(Team_Id)
)

CREATE TABLE IF NOT EXISTS season_summaries (
	Season Integer, 
	Num_Teams Integer,
	Champion_Team_Id Integer,
	Runner_Up_Team_Id Integer,
	Highest_Total_Points_Team Integer,
	Avg_Weekly_Score Numeric,
	Foreign Key (Season) References teams_season(Season)
)