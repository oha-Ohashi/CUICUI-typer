import json
def generate_res(name, switch, payload):
	print(name, switch, payload)
	if name == "Unknown":
		res = {
			"waku1": "くいくいタイパー",
			"waku2": name,
			"waku3": "名前を入力してください。",
			"waku4": "",
			"waku5": "",
			"waku6": ""
		}
		return json.dumps(res, ensure_ascii=False)
	else:
		return "mimi"