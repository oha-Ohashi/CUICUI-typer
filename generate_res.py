import json
import glob, os, shutil
def generate_res(param):
	print(param)
	if param['name'] == "Unknown":
		if param['switch'] == 'false' and param['enter'] == 'true':
			path_user = './cuicui/users/'+ param['payload'] +'.json'
			name_list = get_users()
			if not param['payload'] in name_list:
				shutil.copy(
					'./cuicui/users/default.json', 
					path_user
				)
				
				d = {}
				with open(path_user, 'r', encoding='utf-8') as f:
					d = json.load(f)
				d['waku2'] = param['payload']
				with open(path_user, 'w', encoding='utf-8') as f:
					json.dump(d, f, ensure_ascii=False, indent=2)

			res = {}
			with open(path_user, 'r', encoding='utf-8') as f:
				res = json.load(f)

		else:
			res = {
				"waku1": "くいくいタイパー",
				"waku2": param['name'],
				"waku3": "名前を入力してください。",
				"waku4": "",
				"waku5": "",
				"waku6": ""
			}
		return json.dumps(res, ensure_ascii=False)
	else:
		return "mimi"

def get_users():
	res = []
	for path in glob.glob('./cuicui/users/*.json'):
		basename_without_ext = os.path.splitext(os.path.basename(path))[0]
		res.append(basename_without_ext)
	print(res)
	return res