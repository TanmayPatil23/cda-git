import lichess.api as api 
from lichess.format import JSON, PGN, PYCHESS
import pandas as pd 
import json 
from access_token_lichess import token
import os 


def get_pgn_games(user: str, maxn: int):
	games = api.user_games(user, max=maxn, format=PGN)
	return games

def get_single_pgn(id: str):
	pgn = api.game(id, format=PGN)
	return pgn


def print_board(id: str):
	game = api.game(id, format=PYCHESS)
	print(game.end().board())
	return

def get_user_stats(username: str):
	stats = api.user(username)
	return stats

def get_users_by_team(teamname: str):
	users = api.users_by_team(teamname)
	return users

def get_status(userlist: list):
	status = []
	ret = api.users_status(userlist)
	for stat in ret:
		status.append(ret)	
	return status	

def get_moves(id: str):
	game = api.game(id)
	moves = game['moves']
	return moves

def get_live_tournaments():
	return api.tournaments()


if __name__ == '__main__':
	# print(os.getcwd())
	# api.users_by_team
	gms = {'Magnus Carlsen': 'DrNykterstein', 'Alireza Firouzja' : 'alireza2003', 'Fabiano Caruana' : 'Bombegranate', 'Anish Giri': 'AnishGiri', 'Wesley So' : 'gmwesleyso1993'}
	users = ['Zhigalko_Sergei', 'Drvitman', 'Durarbayli', 'RealDavidNavara', 'EricRosen', 'RebeccaHarris', 'C9C9C9C9C9', 'nihalsarin2004', 'Jaggust01', 'Blazinq', 'Arka50', 'ARM-777777', 'hansontwitch', 'MasterAssasin123', 'chessmaster2006']

	for i in gms.keys():
		users.append(gms[i])

	for user in users:
		filename = os.getcwd()+ '/' + user + '.json'
		file = open(filename, 'w')
		games = api.user_games(user , max=500, format=JSON)
		json.dump(list(games), file, indent=3)
		file.close()

	# for user in users:
	# 	games = api.user_games(user, max=1, format=JSON)
	# 	json.dump(*list(games), file, indent=3)

	# users = api.users_by_team('agadmators-team')
	# print(len(list(users)))
	# print(json.dumps(*list(users), indent=5))

	# games = api.users_games() 
	# file = open('tmp.json', 'w') 
	# json.dump(game, file, indent=5) # df = pd.DataFrame(game) # print(df.head()) 
	# # print(game) 
	# file.close()