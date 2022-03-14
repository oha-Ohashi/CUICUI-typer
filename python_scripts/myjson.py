import json
import time

def path_itc(arg):
	return './cuicui/data/instances/'+arg+'.json'

def json_to_dict(path):
	#while(myread(path) == ""):
		#print("|", end='')
	while True:
		try:
			res = json.loads(myread(path))
			return res
			break
		except:
			print("myjson.pyでjson.loadsに失敗。")
			time.sleep(0.05)
	#return json.loads(myread(path))

def dict_to_json(path, data):
	with open(path, 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)

def myread(path):
	return open(path, 'r', encoding='utf-8').read()