import time
import myjson

def get_player_dict(path, bot_name):
	itc_dict = myjson.json_to_dict(path)
	res = {}
	for i, p in enumerate(itc_dict['players']):
		if p['name'] == bot_name:
			res = p
	return res

def bot_switch(itc_dict, phase, pl_dict):
	if phase == 0:
		do_it("準備完了")
	elif phase >= len(itc_dict['thread']) - 1:
		print("終わったねぇ")
	else:
		do_it(itc_dict['thread'][phase])

def do_it(s):
	for c in s:
		print(c)
		time.sleep(0.5)

def bot_life(path, bot_name):
	while get_player_dict(path, bot_name)['active']:
		itc_dict = myjson.json_to_dict(path)
		pl_dict = get_player_dict(path, bot_name)
		gph = itc_dict['global-phase']
		lph = pl_dict['local-phase']
		if gph == lph:
			bot_switch(itc_dict, gph, pl_dict)
		

		# 条件が揃ったらactiveをfalseに
	
	print("dead:", bot_name)