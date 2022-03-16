import json
import time
import glob, os, shutil
from . import myjson
import random
random.seed(0)

from . import gameinstance
itc_store = []


def generate_res(param):
	res = "(server)default response."
	# パラメーターを列挙
	'''
	for i in range(len(param)):
		print(i, end=":")
		print(param[i], end='(')
		print(type(param[i]), end=')  ')
	print()
	'''

	if param[0] == "name":
		if type(param[1]) is str and len(param[1]) > 0 and len(param[1]) < 16:
			res = "お名前設定:"+ param[1]

	if param[0] == "view":
		res = ""
		itc_list = get_itc_names()
		if len(itc_list) == 0:
			res = "既存インスタンスがありません。新規作成してください。"
		else:
			for i in range(len(itc_list)):
				res += str(i) + ": "
				res += itc_list[i] + "<br>"

	if param[0] == "create":
		itc_list = get_itc_names()
		if type(param[1]) is str and len(param[1]) > 0 and len(param[1]) <= 16:
			if not param[1] in itc_list:
				#インスタンスを追加 
				game = gameinstance.Game(param[1])
				itc_store.append(game)
				game.start_tick()
				game.start_facilitator()
				game.start_write()    ######本番では消す########
				res = "対戦インスタンス `"+ param[1] +" `が無事開かれました。"
				res += "<br>1分間インスタンス情報の更新がない場合、インスタンスは自動的に削除されます。"
			else:
				res = "すでに同名のインスタンスがあります。"
		else:
			res = "コマンドまたはインスタンス名が不正です。"

	# 0:'join' 1:game 2:name
	if param[0] == "join":
		if type(param[1]) is str:
			if(len(param[2]) > 0):
				game = pick_an_instance(param[1])
				if game != -1:
					res = game.add_player(param[2])
				else:
					res = param[1] + ": そのようなインスタンスはありません。"
			else:
				res = "プレイするにはお名前を登録してください。"
		else: 
			res = "コマンドが不正です。"
	
	# 0:'bot' 1:level 2:name 3:instance
	if param[0] == "bot":
		if int(param[1]) in list(range(1,11)):
			game = pick_an_instance(param[3])
			if game != -1:
				res = game.add_bot(param[1])    ### botを追加
			else:
				res = "botを追加するにはインスタンスに参加してください。"
		else:
			res = "コマンドが不正です。"

	if param[0] == "wip":	#1:input 2:name 3:instance
		game = pick_an_instance(param[3])
		#print(game)
		player = pick_an_player(param[2], game)
		player['wip'] = param[1]
	if param[0] == "sync":	#1:None 2:name 3:instance
		li = create_odai_and_disp(param[3], param[2])
		res = '\\'.join(li)
			
	if param[0] == "test":
		res = "(サーバー)これはてすとだよ"
	if param[0] == "clear":
		clear_instances()
		res = "[裏コマ]インスタンス全消ししたで"

	return res


def get_itc_names():
	res = list(map(lambda p: p.data['itc_name'], itc_store))
	return res
def pick_an_instance(name):
	for x in itc_store:
		if x.data['itc_name'] == name:
			return x
	return -1
def pick_an_player(name, game):
	for p in game.data['players']:
		if p['name'] == name:
			return p
	return -1

def clear_instances():
	global itc_store
	for game in itc_store:
		game.kill()
		itc_store.remove(game)
		#del itc_store[i]
	
def iru(itc_dict, name):
	res = False
	for p in itc_dict['players']:
		if p['name'] == name:
			res = True
	return res

def create_odai_and_disp(itc_name, name):
	res = ["<br>", "<br><br><br>"]
	game = pick_an_instance(itc_name)
	if game != -1:
		res[1] += create_disp(game)
		player = pick_an_player(name, game)
		res[0] += game.data['thread'][game.data['global-phase']]
		return res
	return ["こりゃ","だめだ"]

def create_disp(game):
	res = ""
	###################ここに得点順のソートをそーにゅう###########
	for p in game.data['players']:
		res += "score "+  str(p['score']) + ": " + p['name'] + "<br>"
		res += "&ensp;" + p['wip'] + "<br>"
	return res
