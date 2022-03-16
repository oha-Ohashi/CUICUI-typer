import json
import time
import random
import threading
from . import facilitator, bot


class Game():
	def __init__(self, itc_name):
		self.data = {
			"itc_name": itc_name,
			"json_path": "./cuicui/data/instances/"+itc_name+".json",
			"thread": [
				"｢準備完了｣とタイプしてそのままお待ちください。<br>Enterを押すと入力内容がリセットされます。",
				"あいうえお",
				"かきくけこ",
				"[対戦終了]お疲れさまでした。<br>F5キーで退出してください。"
			],
			"alive": True,
			"clock": 0,
			"footprint": time.time(),
			"global-phase": 0,
			"players":[]
		}
	
	def create_thread(self, n):
		words = ["ああ言えばこう言う","急がば回れ","魚心あれば水心","縁の下の力持ち","鬼の目にも涙","飼い犬に手を噛まれる","九死に一生を得る","口は禍の元","芸術は長く人生は短し","後悔先に立たず","猿も木から落ちる","知らぬが仏","酸いも甘いも噛み分けた","善は急げ","大は小を兼ねる","塵も積もれば山となる","鶴は千年亀は万年","天は二物を与えず","時は金なり","長い物には巻かれろ","二度あることは三度ある","糠に釘","猫の手も借りたい","暖簾に腕押し","早起きは三文の徳","火のないところに煙は立たぬ","覆水盆に反らず","弁慶の泣き所","仏の顔も三度","眉毛を読まれる","身から出た錆","娘一人に婿八人","目には目、歯には歯","元の鞘に納まる","焼け石に水","油断大敵","弱り目に祟り目","楽は苦の種、苦は楽の種","良薬は口に苦し","類は友を呼ぶ","例によって例の如し","論語読みの論語知らず","笑う門には福来たる"]
		lst = list(range(0, len(words)))
		index_list = random.sample(lst, n)
		words_to_type = list(map(lambda i:words[i], index_list))
		#print(words_to_type)
		thread = [
			"｢準備完了｣とタイプしてそのままお待ちください。<br>Enterを押すと入力内容がリセットされます。",
		]
		for w in words_to_type:
			thread.append(w)
		thread.append("[対戦終了]お疲れさまでした。<br>F5キーで退出してください。")
		#print(thread)
		self.data['thread'] = thread

	def add_player(self, name):
		existing = list(map(lambda p: p['name'], self.data['players']))
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
		thread = threading.Thread(
			target=bot.bot_life,
			args=(self, player_dict,)
		)
		thread.start()
		return bot_name + "が参加しました。<br>"
		
	def start_tick(self):
		thread = threading.Thread(target=self.tick)
		thread.start()
	def tick(self):
		while self.data['alive']:
			time.sleep(0.5)
			self.data['clock'] += 0.5
		print("incliment done")
	
	def start_facilitator(self):
		thread = threading.Thread(target=self.facilitator)
		thread.start()
	def facilitator(self):
		while self.data['alive']:
			time.sleep(0.01)
			#facilitator.printit(self)
			facilitator.incliment_local_phase(self)

	def footprint(self):
		self.data['footprint'] = time.time()
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