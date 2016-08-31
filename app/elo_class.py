class elo_score_generator(object):
		"""docstring for elo_score_generator"""
		def __init__(self, data):
			self.data = data
			
		def get_most_popular_characters(self):
			chars = {i for i in self.data.char1}
			chars |= {i for i in self.data.char2}
			chars = {char: 0 for char in chars}
			character_cols = [self.data.char1, self.data.char2]
			for char in character_cols:
				for character in chars:
					chars[character] += [i for i in char].count(character)
			return chars

		def gen_elo_scores(self, p1Col, p2Col, winnerCol, loserCol):
			'''Takes 4 arguments:
				p1Col - column for 1st player
				p2Col - column for 2nd player
				winnerCol - Column for match winner
				loserCol - Column for match loser

				Performs an augmented ELO rating opertion where, instead of gaining points if a player loses,
					players lose points if they lose.
				This is to balance the nature of points lost/gained
			'''
			elo_dict = {key for key in p1Col}; elo_dict |= {key for key in p2Col}
			elo_dict = {key : 100 for key in elo_dict} # Generate starting score dicitonary for the period
			match_ups = [sorted((x,y)) for x,y in zip([i for i in p1Col], [i for i in p2Col])] # Gen match keys
			match_ups = {"_vs_".join(key) : 0 for key in match_ups} # Match log dictionary to keep count of unique matches
			games_played = {key : 0 for key in elo_dict}
			winner_elo_score = [0]*len(self.data)
			loser_elo_score = [0]*len(self.data)
			# match_counter = [0]*len(self.data)
			winners = tuple(i for i in winnerCol)
			losers = tuple(i for i in loserCol)
			
			for index in range(len(winners)):
				winner = winners[index]
				loser = losers[index]
				
				match = "_vs_".join(sorted((winner, loser)))
				match_ups[match] += 1
				games_played[winner] += 1
				games_played[loser] += 1
				match_count = match_ups[match]

				# Add wins
				opp_rating = elo_dict[loser] + (elo_dict[loser]//4)
				perf_rating = int(opp_rating/games_played[winner])
				elo_dict[winner] += perf_rating

				# Subtract losses
				opp_rating = elo_dict[winner] - (elo_dict[winner]//4)
				perf_rating = int(opp_rating/games_played[loser])
				elo_dict[loser] -= perf_rating

				elo_dict[loser] = 100 if elo_dict[loser] < 100 else elo_dict[loser]
				elo_dict[winner] = 2600 if elo_dict[winner] > 2600 else elo_dict[winner]
				
				winner_elo_score[index] = elo_dict[winner]
				loser_elo_score[index] = elo_dict[loser]

			return elo_dict

		def get_char_win_loss(self):
			p1 = [i for i in self.data.p1]
			p2 = [i for i in self.data.p2]
			char1 = [i for i in self.data.char1]
			char2 = [i for i in self.data.char2]
			winner = [i for i in self.data.winnerID]
			winningChar = [None]*len(self.data)
			losingChar = [None]*len(self.data)

			for i in range(len(self.data)):
				if p1[i] == winner[i]:
					winningChar[i] = char1[i]
					losingChar[i] = char2[i]
				else:
					winningChar[i] = char2[i]
					losingChar[i] = char1[i]

			self.data["winningChar"] = winningChar
			self.data["losingChar"] = losingChar