import glob, os
import time, threading
import myjson, game

class Watcher:
	def __init__(self, itc_name):
		self.itc_name = itc_name
		self.itc_path = "../data/instances/"+self.itc_name+".json"
		self.thread = threading.Thread(target=self.watch)
		self.thread.start()

	def watch(self):
		itc_dict_prev = myjson.json_to_dict(self.itc_path)
		while(myjson.json_to_dict(self.itc_path)["alive"]):
			itc_dict_now = myjson.json_to_dict(self.itc_path)
			if(itc_dict_now != itc_dict_prev):
				time.sleep(0.1)
				game.anychange(itc_dict_now)
				#print(itc_dict_now)
			itc_dict_prev = itc_dict_now

def get_instances():
	res = []
	for path in glob.glob('../data/instances/*.json'):
		basename_without_ext = os.path.splitext(os.path.basename(path))[0]
		res.append(basename_without_ext)
	#print(res)
	return res


if __name__ == '__main__':
	list_prev = []
	watchers = {}
	while True:
		list_now = get_instances()
		list_now.remove('default')
		if list_prev != list_now:
			print('deference detected.')
			if len(list_now) > len(list_prev):
				start_them = list(set(list_now) - set(list_prev))
				print('start them:', start_them)
				for item in start_them:
					watchers[item] = Watcher(item)
			else:
				stop_them = list(set(list_prev) - set(list_now))
				print('stop_them:', stop_them)
				for item in stop_them:
					del watchers[item]
		list_prev = list_now
		#time.sleep(0.1)
		#print(".")
