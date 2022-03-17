import time
import random

class Bot():
	def __init__(self, game, bot_dict):
		self.game = game
		self.bot_dict = bot_dict
		self.delay_head = [4,3.5,3,3,2.5,  2,1.5,1.0,0.7,0.5]
		self.delay_mean = [3,2,1.5,1.0,0.7,  0.5,0.4,0.3,0.2,0.1]

	def bot_switch(self):
		phase = self.game.data['global-phase']
		if phase == 0:
			self.bot_type("準備完了")
		elif phase >= len(self.game.data['thread']) - 1:
			#print("bot_switch:終わったねぇ")
			pass
		else:
			#print(self.game.data['thread'][phase])
			self.bot_type(self.game.data['thread'][phase])

	def bot_type(self, string):
		wip = ""
		level = int(self.bot_dict["level"]) - 1
		time.sleep(self.delay_head[level])
		for c in string:
			wip += c
			print(c)
			self.bot_dict['wip'] = wip
			time.sleep(self.randomize(self.delay_mean[level]))

	def randomize(self, span):
		proportion = 0.3
		minimum = span - (span * proportion)
		maximum = span + (span * proportion)
		return random.uniform(minimum, maximum)


def bot_life(game, bot_dict):
	bot = Bot(game, bot_dict)
	while game.data['alive']:
		gph = game.data['global-phase']
		lph = bot_dict['local-phase']
		if gph == lph:
			bot.bot_switch()

	print("dead:", bot_name)
