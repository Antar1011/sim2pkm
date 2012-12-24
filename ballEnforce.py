from lookup import *

eventmove = {'Celebi': {'moves': ['nastyplot'], 'shiny': False, 'ball':'cherish'},
	'Charmander': {'moves': ['quickattack','howl'], 'shiny': False, 'ball':'cherish'},
	'Mew': {'moves': ['teleport'], 'shiny': False, 'ball':'cherish'},
	'Entei': {'moves': ['crushclaw', 'extremespeed', 'flareblitz', 'howl'], 'shiny': True, 'ball':'cherish'},
	'Salamence': {'moves': ['dragondance', 'hydropump'], 'shiny': False, 'ball':'cherish'},
	'Pikachu': {'moves': ['teeterdance', 'yawn', 'sing', 'extremespeed', 'lastresort'], 'ball':'cherish'},
	'Meowth': {'moves': ['sing'], 'shiny': False, 'ball':'cherish'},
	'Suicune': {'moves': ['sheercold','aquaring','extremespeed','airslash'], 'shiny': True, 'ball':'cherish'},
	'Mewtwo': {'moves': ['electroball'], 'shiny': False, 'ball':'cherish'},
	'Jirachi': {'moves': ['dracometeor'], 'shiny': False, 'ball':'cherish'},
	'Piplup': {'moves': ['sing'], 'shiny': False, 'ball':'cherish'},
	'Victini': {'moves': ['fusionflare','boltstrike','glaciate','vcreate','blueflare','fusionbolt'], 'shiny': False, 'ball':'cherish'},
	'Arceus': {'moves': ['roaroftime','spacialrend','shadowforce'], 'shiny': False, 'ball':'cherish'},
	'Snivy': {'moves': ['aromatherapy'], 'shiny': False, 'ball':'cherish'},
	'Zekrom': {'moves': ['haze'], 'shiny': False, 'ball':'cherish'},
	'Rayquaza': {'moves': ['vcreate'], 'shiny': False, 'ball':'cherish'},
	'Raikou': {'moves': ['extremespeed','aurasphere','weatherball','zapcannon'], 'shiny': True, 'ball':'cherish'},
	'Pichu': {'moves': ['endeavor'], 'shiny': True, 'ball':'cherish'},
	'Darkrai': {'moves': ['spacialrend','roaroftime'], 'shiny': False, 'ball':'cherish'},
	'Reshiram': {'moves': ['mist'], 'shiny': False, 'ball':'cherish'},
	'Audino': {'moves': ['present'], 'ball':'cherish'},
	'Heatran': {'moves': ['eruption'], 'shiny': False, 'ball':'pokeball'}}

pokemove = {}

cherishonly = ['Keldeo', 'Meloetta', 'Genesect']

dreamradar = {'Riolu': 'prankster',
	'Lucario': 'justified',
	'Tornadus': 'defiant',
	'Tornadus-Therian': 'defiant',
	'Thundurus': 'defiant',
	'Thundurus-Therian': 'defiant',
	'Landorus': 'sheerforce',
	'Landorus-Therian': 'sheerforce',
	'Dialga': 'telepathy',
	'Palkia': 'telepathy',
	'Giratina': 'telepathy',
	'Ho-Oh': 'regenerator',
	'Lugia': 'multiscale'}

def ballEnforce(poke):
	ball = 'pokeball'
	nonick = False
	shiny = poke['shiny']
	if poke['species'] in cherishonly:
		ball = 'cherish'
		nonick = True
		#print poke['species']+' is cherish-only'
	if 'sketch' not in movepool[keyify(poke['species'])]:
		for move in poke['moves']:
			if move in movepool[keyify(poke['species'])]:
				if poke['species'] in eventmove:
					if move in eventmove[poke['species']]['moves']:
						ball = eventmove[poke['species']]['ball']
						nonick = True
						if 'shiny' in eventmove[poke['species']]:
							shiny = eventmove[poke['species']]['shiny']
			else:
				ball = 'cherish'
				print move+' is illegal on '+poke['species']
				break

	if ball == 'pokeball':
		if poke['species'] in dreamradar:
			if poke['ability'] == dreamradar[poke['species']]:
				ball = 'dream'

	return [ball,nonick,shiny]
