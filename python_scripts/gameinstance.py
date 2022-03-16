import json
import time
import threading


class Game():
	def __init__(self, itc_name):
		self.data = {
			"itc_name": itc_name,
			"json_path": "./cuicui/data/instances/"+itc_name+".json",
			"alive": True,
			"thread": ['a','b','c'],
			"clock": 0,
			"time": 0,
			"global-phase": 0,
			"players":[]
		}

	def add_player(self, name):
		existing = list(map(lambda e:e['name'], self.data['players']))
		if not name in existing:
			player_dict = {
				"name": name,
				"bot" : False,
				"local-phase": 0,
				"score": 0,
				"wip": ""
			}
			self.data['players'].append(player_dict)
			return "[成功]インスタンス:"+self.data['itc_name']+":に新しく参加しました。<br>`助けてい`:インスタンス操作のコマンドを見る"
		else:
			return "[成功]インスタンス:"+self.data['itc_name']+":に移動しました。<br>`助けてい`:インスタンス操作のコマンドを見る"

	def add_bot(self, level):
		bot_tag = "#"+ str(int((time.time() * 100) % 100000))
		bot_name = "bot-Lv" + str(level) + bot_tag
		player_dict = {
			"name": bot_name,
			"bot" : True,
			"level": level,
			"local-phase": 0,
			"score": 0,
			"wip": ""
		}
		self.data['players'].append(player_dict)
		return bot_name + "が参加しました。<br>"
		
	def start_tick(self):
		thread = threading.Thread(target=self.tick)
		thread.start()
	def tick(self):
		while self.data['alive']:
			time.sleep(0.5)
			self.data['clock'] += 0.5
			self.data['time'] += time.time()
		print("incliment done")

	def kill(self):
		self.data['alive'] = False

	def start_write(self):
		thread = threading.Thread(target=self.write)
		thread.start()
	def write(self):
		while self.data['alive']:
			#print(json.dumps(self.data))
			with open(self.data["json_path"], 'w', encoding='utf-8') as f:
				json.dump(self.data, f, indent=2, ensure_ascii=False)
			time.sleep(0.1)
		with open(self.data["json_path"], 'w', encoding='utf-8') as f:
			json.dump(self.data, f, indent=2, ensure_ascii=False)
		time.sleep(0.1)