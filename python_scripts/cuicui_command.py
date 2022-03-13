import json
import time
import glob, os, shutil
from . import myjson
def generate_res(param):
	res = "default response."
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
			res += "<br>5分間インスタンス情報の更新がない場合、インスタンスは自動的に削除されます。"
		else:
			res = "すでに同名のインスタンスがあります。"

	if param[0] == "join":
		itc_list = get_instances()
		if param[1] in itc_list:
			itc_path = myjson.path_itc(param[1])
			itc_dict = myjson.json_to_dict(itc_path)
			itc_dict['players'][param[2]] = json.load(open('./cuicui/data/player.json', 'r', encoding='utf-8'))
			#print(itc_dict)
			myjson.dict_to_json(itc_path, itc_dict)
			res = "[成功]インスタンス`"+param[1]+"`に参加しました。"
		else:
			res = param[1] + ": そのようなインスタンスはありません。"
			
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
		time.sleep(0.5)
		os.remove(itc_path)