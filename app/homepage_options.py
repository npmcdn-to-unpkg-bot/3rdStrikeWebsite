'''
Edits here adjust home page parameters.

"start_date/end_date" adjusts the query period for the homepage leaderboard
"leagues" adjusts which leagues are sought.
'''

def gen_results(start_date=None, end_date=None, leagues=[]):
	from pandas import Series, DataFrame
	from app.munge_data import main as generate_rankings
	results_data = {l: {} for l in leagues}
	for l in results_data.keys():
		results_data[l]["player_elo"], results_data[l]["char_elo"], results_data[l]["data"] =\
			generate_rankings(start_date, end_date, l)
		
		playerElo = results_data[l]["player_elo"]
		players = Series([i for i in playerElo.keys()])
		raw_data = results_data[l]["data"]
		wins = [i for i in raw_data.winnerID]
		losses = [i for i in raw_data.loserID]
		del results_data[l]["data"]
		
		data = DataFrame(players, columns=["playerName"])
		data["eloScore"] = [playerElo.get(p) for p in data.playerName]
		data["wins"] = [wins.count(p) for p in data.playerName]
		data["losses"] = [losses.count(p) for p in data.playerName]
		data = data.sort_values(by=["eloScore", "wins", "losses"], ascending=[False, False, True]).copy()

		results_data[l]["players"] = [i for i in data.playerName]
		results_data[l]["eloScore"] = [i for i in data.eloScore]
		results_data[l]["wins"] = [i for i in data.wins]
		results_data[l]["losses"] = [i for i in data.losses]
		del playerElo, data, players
	return results_data