import json
import time
import glob, os, shutil
from . import myjson
import random
random.seed(0)


def generate_res(param):
	res = "(server)default response."
	# パラメーターを列挙
	for i in range(len(param)):
		print(i, end=":")
		print(param[i], end='  ')
	print()

	if param[0] == "view":
		res = ""
		itc_list = get_instances()
		itc_list.remove("default")
		if len(itc_list) == 0:
			res = "既存インスタンスがありません。新規作成してください。"
		else:
			for i in range(len(itc_list)):
				res += str(i) + ": "
				res += itc_list[i] + "<br>"

	if param[0] == "create":
		itc_list = get_instances()
		if not param[1] in itc_list:
			shutil.copy(
				'./cuicui/data/instances/default.json',
				'./cuicui/data/instances/'+ param[1] +'.json'
			)
			res = "対戦インスタンス `"+ param[1] +" `が無事開かれました。"
			res += "<br>1分間インスタンス情報の更新がない場合、インスタンスは自動的に削除されます。"
		else:
			res = "すでに同名のインスタンスがあります。"

	if param[0] == "join":
		itc_list = get_instances()
		if param[1] in itc_list:
			itc_path = myjson.path_itc(param[1])
			itc_dict = myjson.json_to_dict(itc_path)
			player = myjson.json_to_dict('./cuicui/data/player.json')
			if not iru(itc_dict=itc_dict, name=param[2]):
				player["name"] = param[2]
				itc_dict['players'].append(player)
				myjson.dict_to_json(itc_path, itc_dict)
				res = "[成功]インスタンス`"+param[1]+"`に新しく参加しました。<br>`助けてい`:インスタンス操作のコマンドを見る"
			else:
				res = "[成功]インスタンス`"+param[1]+"`に移動しました。<br>`助けてい`:インスタンス操作のコマンドを見る"
		else:
			res = param[1] + ": そのようなインスタンスはありません。"
	
	if param[0] == "bot": # 1:instance 2:level
		itc_path = myjson.path_itc(param[1])
		itc_dict = myjson.json_to_dict(itc_path)
		bot = myjson.json_to_dict('./cuicui/data/bot.json')
		#bot_tag = "#"+ str(random.randint(0,9999))
		# 123.45秒→12345
		bot_tag = "#"+ str(int((time.time() * 100) % 100000))
		bot_name = "bot-Lv" + str(param[2]) + bot_tag
		bot["name"] = bot_name
		bot["level"] = param[2]
		itc_dict["players"].append(bot)
		myjson.dict_to_json(itc_path, itc_dict)
		res = bot_name + "が参加しました。<br>"
		time.sleep(0.5)

	if param[0] == "wip":	#1:instance 2:name 3:input
		player_property_update(param[1], param[2], ["wip", param[3]])
	if param[0] == "sync":	#1:instance 2:name
		li = create_odai_and_disp(param[1], param[2])
		res = ','.join(li)
			
	if param[0] == "test":
		res = "(サーバー)これはてすとだよ"
	if param[0] == "clear":
		clear_instances()

	return res


def get_instances():
	res = []
	for path in glob.glob('./cuicui/data/instances/*.json'):
		basename_without_ext = os.path.splitext(os.path.basename(path))[0]
		res.append(basename_without_ext)
	#print(res)
	return res

def clear_instances():
	itc_list = get_instances()
	itc_list.remove("default")
	for item in itc_list:
		itc_path = myjson.path_itc(item)
		itc_dict = myjson.json_to_dict(itc_path)
		itc_dict['alive'] = False
		myjson.dict_to_json(itc_path, itc_dict)
		time.sleep(1)
		os.remove(itc_path)
	
def iru(itc_dict, name):
	res = False
	for p in itc_dict['players']:
		if p['name'] == name:
			res = True
	return res

def player_property_update(instance, name, key_and_value):
	for item in get_instances():
		if item ==  instance:
			itc_path = myjson.path_itc(instance)
			itc_dict = myjson.json_to_dict(itc_path)
			for i, p in enumerate(itc_dict['players']):
				if p['name'] == name:
					itc_dict['players'][i][key_and_value[0]] = key_and_value[1]			

			myjson.dict_to_json(itc_path, itc_dict)
	print(key_and_value)

def create_odai_and_disp(instance, name):
	res = ["<br>", "<br><br><br>"]
	for item in get_instances():
		if item == instance:
			itc_path = myjson.path_itc(instance)
			itc_dict = myjson.json_to_dict(itc_path)
			res[1] += create_disp(itc_dict)
			for i, p in enumerate(itc_dict['players']):
				if p['name'] == name:
					res[0] += itc_dict['thread'][itc_dict['global-phase']]
	return res

def create_disp(itc_dict):
	res = ""
	for i, p in enumerate(itc_dict['players']):
		#res += p['name'] + ": score " + str(p['score']) + "<br>"
		res += "score "+  str(p['score']) + ": " + p['name'] + "<br>"
		res += "&ensp;" + p['wip'] + "<br>"
	return res
