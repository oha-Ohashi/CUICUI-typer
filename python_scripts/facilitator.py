
def printit(obj):
	print(type(obj))
	obj.data['clock'] += 1

def incliment_local_phase(game):
	for p in game.data['players']:
		if p['local-phase'] == 0:
			if p['wip'] == "準備完了" or p['wip'] == "ready":
				print("\n\nででどん\n\n")
				p['local-phase'] += 1
				incliment_global_phase(game)
		elif p['local-phase'] == len(game.data['thread']) - 1:
			#print(p['name'], "打ち終わり")
			pass
		else:
			if p['wip'] == game.data['thread'][p['local-phase']]:
				p['local-phase'] += 1
				p['score'] += some_point(game, p)
				incliment_global_phase(game)

def some_point(game, player):
	local_phases = list(map(lambda p: p['local-phase'],  game.data['players']))
	#print(local_phases)
	position = local_phases.count(player['local-phase'])
	#print("position: ", position)

	#ポイント加算
	point_list = [0,100,75,50,25,0]
	if position > 5:  #メンバーが多かった時に切る
		position = 5
	return point_list[position]

def incliment_global_phase(game):
	local_phases = list(map(lambda p: p['local-phase'],  game.data['players']))
	if len(set(local_phases)) == 1:
		game.data['global-phase'] += 1
