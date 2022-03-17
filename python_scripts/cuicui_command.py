import json
import time
import glob, os, shutil
import random
random.seed(0)

from . import gameinstance
itc_store = []

help_text = [
	[
		"名前 `名前`: ユーザーネームを`名前`に設定",
		"一覧: 現在開いている対戦インスタンスを表示",
		"作る `名前`: 対戦インスタンス`名前`を作成",
		"入る `名前`: 対戦インスタンス`名前`に入室する"
	],
	[
		"Tabキー: コマンドエリアとタイピングエリアを往復",
		"`リスト` [ことわざ, quotes]: ワードリストを変更",
		"`bot 弱`: おまかせbotブレンド4個体(弱)",
		"`bot 中`: おまかせbotブレンド4個体(中)",
		"`bot 強`: おまかせbotブレンド4個体(強)",
		"`bot [1-10]`: botを1個体だけ追加。レベルは10段階"
	]
]

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

	if param[0] == "助けて":
		res = ""
		for h in help_text[0]:
			res += h + "<br>"
	if param[0] == "助けてい":
		res = ""
		for h in help_text[1]:
			res += h + "<br>"
	if param[0] == "名前":
		if type(param[1]) is str and len(param[1]) > 0 and len(param[1]) < 16:
			res = "お名前設定:"+ param[1]

	if param[0] == "一覧":
		res = ""
		itc_list = get_itc_names()
		if len(itc_list) == 0:
			res = "既存インスタンスがありません。新規作成してください。"
		else:
			for i in range(len(itc_list)):
				res += str(i) + ": "
				res += itc_list[i] + "<br>"

	if param[0] == "作る":
		itc_list = get_itc_names()
		if type(param[1]) is str and len(param[1]) > 0 and len(param[1]) <= 16:
			if not param[1] in itc_list:
				#インスタンスを追加 
				game = gameinstance.Game(param[1])
				if len(itc_store) > 1000:
					itc_store.pop(0)
				itc_store.append(game)
				game.create_thread("ことわざ", 7)
				game.start_tick()
				game.start_facilitator()
				if game.data['itc_name'] == "a":
					game.start_write()  
				res = "対戦インスタンス `"+ param[1] +" `が無事開かれました。"
				res += "<br>5分間打鍵がない場合、インスタンスは自動的に削除されます。"
			else:
				res = "すでに同名のインスタンスがあります。"
		else:
			res = "コマンドまたはインスタンス名が不正です。"

	# 0:'join' 1:game 2:name
	if param[0] == "入る":
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
		
	# 0:'リスト' 1:which one 2:name 3:instance
	if param[0] == "リスト":
		if param[1] in ["ことわざ", "quotes"]:
			game = pick_an_instance(param[3])
			if game != -1:
				game.create_thread(param[1], 7)
				res = "リストを設定しました。"
			else:
				res = "リストを設定するにはインスタンスに参加してください。"
		else:
			res = "コマンドが不正です。"
	
	# 0:'bot' 1:level 2:name 3:instance
	if param[0] == "bot" and isint(param[1]):
		if int(param[1]) in list(range(1,11)):
			game = pick_an_instance(param[3])
			if game != -1:
				res = game.add_bot(param[1])    ### botを追加
			else:
				res = "botを追加するにはインスタンスに参加してください。"
		else:
			res = "コマンドが不正です。"
	if param[0] == "bot" and param[1] in ["弱","中","強"]:
		res = ""
		strength_map = [
			[1,2,3,4],
			[3,4,5,6],
			[7,8,9,10]
		]
		sm = strength_map[["弱","中","強"].index(param[1])]
		for s in sm:
			game = pick_an_instance(param[3])
			if game != -1:
				res += game.add_bot(s)
			else:
				res = "botを追加するにはインスタンスに参加してください。"

	if param[0] == "wip":	#1:input 2:name 3:instance
		game = pick_an_instance(param[3])
		#print(game)
		player = pick_an_player(param[2], game)
		player['wip'] = param[1]
		game.footprint()	     	########footprint#########
	if param[0] == "sync":	#1:None 2:name 3:instance
		li = create_odai_and_disp(param[3], param[2])
		res = '\\'.join(li)
			
	if param[0] == "test":
		res = "(サーバー)これはてすとだよ"
	if param[0] == "clearth":
		clear_instances()
		res = "[裏コマ]インスタンス全消ししたで"

	if not param[0] in ["wip", "sync"]:
		remove_old_instances()
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
	players = game.data['players']
	players_sorted = sorted(players, key=lambda x:x['score'])
	players_sorted.reverse()
	for p in players_sorted:
		res += "score "+  str(p['score']) + ": " + p['name'] + "<br>"
		res += "&ensp;" + p['wip'] + "<br>"
	return res

def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True


def remove_old_instances():
	print("remove old ones")
	old_list = list(filter(
		lambda game:time.time() - game.data['footprint'] > 60*5, 
		itc_store
	))
	print("itc_store:", itc_store)
	print("old_list:", old_list)
	for old_item in old_list:
		old_item.kill()
		itc_store.remove(old_item)