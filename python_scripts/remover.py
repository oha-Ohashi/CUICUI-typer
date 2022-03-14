import os, time, glob
import myjson


while True:
	path_list = glob.glob('../data/instances/*.json')
	path_list.remove('../data/instances/default.json')
	for path in path_list:
		mtime = os.path.getmtime(path)
		elapsed = int(time.time() - mtime)
		print(path)
		print(elapsed)
		if elapsed > 60:
			itc_dict = myjson.json_to_dict(path)
			itc_dict['alive'] = False
			myjson.dict_to_json(path, itc_dict)
			time.sleep(1)
			os.remove(path)
			print("削除:" + path)

	print('/')
	time.sleep(5)