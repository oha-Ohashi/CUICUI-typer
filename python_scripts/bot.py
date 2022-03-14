import time
import myjson

class Bot():
	def __init__(self, path, bot_name, bot_level):
		self.path = path
		self.bot_name = bot_name
		self.bot_level = int(bot_level)
		print(type(self.bot_level))

	def get_player_dict(self):
		itc_dict = myjson.json_to_dict(self.path)
		res = {}
		for i, p in enumerate(itc_dict['players']):
			if p['name'] == self.bot_name:
				res = p
		return res
	def put_player_dict(self, pl_dict):
		itc_dict = myjson.json_to_dict(self.path)
		for i, p in enumerate(itc_dict['players']):
			if p['name'] == self.bot_name:
				itc_dict['players'][i] = pl_dict
		myjson.dict_to_json(self.path, itc_dict)

	def bot_switch(self, itc_dict, phase, pl_dict):
		if phase == 0:
			self.bot_type("準備完了")
		elif phase >= len(itc_dict['thread']) - 1:
			pl_dict = self.get_player_dict()
			pl_dict['active'] = False
			self.put_player_dict(pl_dict)
			print("bot_switch:終わったねぇ")
		else:
			self.bot_type(itc_dict['thread'][phase])

	def bot_type(self, string):
		wip = ""
		for c in string:
			wip += c
			print(c)
			pl_dict = self.get_player_dict()
			pl_dict['wip'] = wip
			self.put_player_dict(pl_dict)
			time.sleep(0.5)
		'''
		pl_dict = self.get_player_dict()
		pl_dict['local-phase'] += 1
		self.put_player_dict(pl_dict)
		'''

def bot_life(path, bot_name, bot_level):
	bot = Bot(path, bot_name, bot_level)
	while bot.get_player_dict()['active']:
		itc_dict = myjson.json_to_dict(path)
		pl_dict = bot.get_player_dict()
		gph = itc_dict['global-phase']
		lph = pl_dict['local-phase']
		if gph == lph:
			bot.bot_switch(itc_dict, gph, pl_dict)
		

		# 条件が揃ったらactiveをfalseに
	
	print("dead:", bot_name)