from app import config, models
from app.models import *
import pandas as pd
from sqlalchemy import create_engine

def main():
	engine = create_engine('sqlite:///app/database.sqlite')
	con = engine.connect()

	data = pd.read_sql_query("SELECT * FROM matchLog", con=con)

	def get_most_popular_characters():
		chars = {i for i in data.char1}
		chars |= {i for i in data.char2}
		chars = {char: 0 for char in chars}
		character_cols = [data.char1, data.char2]
		for char in character_cols:
			for character in chars:
				chars[character] += [i for i in char].count(character)
		return chars

	def get_leaders(start, end):
		'''Generate leader dictionary'''
		data["date"] = pd.to_datetime(data.date)

	def get_elo_score():
		# get elo score
		pass
	popular_characters = get_most_popular_characters() #returns dict object for reporting

	# most_popular_character = 

if __name__ == '__main__':
	main()