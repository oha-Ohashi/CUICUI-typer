import json
def path_itc(arg):
	return './cuicui/data/instances/'+arg+'.json'
def json_to_dict(path):
	return json.load(open(path, 'r', encoding='utf-8'))
def dict_to_json(path, data):
	with open(path, 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)
