import time
import myjson

def incliment_local_phase(itc_dict, path):
	res = 0
	for i, p in enumerate(itc_dict['players']):
		if p['local-phase'] == 0:
			if p['wip'] == "準備完了":
				itc_dict['players'][i]['local-phase'] += 1
				# global phase 上げ
				itc_dict = incliment_global_phase(itc_dict)
		elif(p['local-phase'] == len(itc_dict['thread']) -1 ):
			print("打ち終わり")
		# 最初でも最後でもない、採点対処のタイプ
		else:
			res = i
			if p['wip'] == itc_dict['thread'][p['local-phase']]:
				itc_dict['players'][i]['local-phase'] += 1
				# ポイント付与、 global phase 上げ
				itc_dict = give_some_point(itc_dict, i)
				itc_dict = incliment_global_phase(itc_dict)
	myjson.dict_to_json(path, itc_dict)

def give_some_point(itc_dict, which_one_passed):
	local_phases = []
	for i, p in enumerate(itc_dict['players']):
		local_phases.append(p['local-phase'])
	print(local_phases)
	position = local_phases.count(local_phases[which_one_passed])
	print("position: ", position)
	'''
	#global-phase上げ
	if position >= len(itc_dict['players']):
		itc_dict['global-phase'] += 1
	'''
	#ポイント加算
	point_list = [0,100,50]
	if position > 2:  #メンバーが多かった時に切る
		position = 2
	itc_dict['players'][which_one_passed]['score'] += point_list[position]
	#myjson.dict_to_json(path, itc_dict)
	return itc_dict

def incliment_global_phase(itc_dict):
	local_phases = []
	for i, p in enumerate(itc_dict['players']):
		local_phases.append(p['local-phase'])
	if len(set(local_phases)) == 1:
		itc_dict['global-phase'] += 1
	return itc_dict
	


def anychange(itc_dict, path):
	print("any change")
	incliment_local_phase(itc_dict, path)
	#give_some_point(itc_dict, path, which_one_passed)

