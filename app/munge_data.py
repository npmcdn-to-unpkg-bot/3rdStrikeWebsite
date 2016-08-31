from app import config, models
from app.models import *
import pandas as pd
from app.elo_class import elo_score_generator
import sqlite3

def main(start_date=None, end_date=None, league=None):
	con = sqlite3.connect('/app/database.sqlite')

	data = pd.read_sql_query("SELECT * FROM matchLog", con=con)

	data["date"] = pd.to_datetime(data.date)

	if start_date and end_date:
		# Shrinking data... 
			# May have to switch to PostGres because 
			# this can get to the point where it's not going to fit in memory
			# and a SQL query on dates will be necessary
		start_mask = data["date"] >= pd.to_datetime(start_date)
		end_mask = data["date"] <= pd.to_datetime(end_date)
		data = data[start_mask & end_mask]

	if league:
		data = data[data.league == league].copy()

	elo_score_gen = elo_score_generator(data=data)
	elo_score_gen.get_char_win_loss()
	popular_characters = elo_score_gen.get_most_popular_characters() #returns dict object for reporting
	final_elo_scores = elo_score_gen.gen_elo_scores(data.p1, data.p2, data.winnerID, data.loserID)
	final_char_elos = elo_score_gen.gen_elo_scores(data.char1, data.char2, 
		data.winningChar, data.losingChar)

	return final_elo_scores, final_char_elos, data

if __name__ == '__main__':
	main()