from lookup import *

cherishmove = {'Celebi': ['nastyplot'],
	'Charmander': ['quickattack','howl'],
	'Mew': ['teleport'],
	'Entei': ['crushclaw', 'extremespeed', 'flareblitz', 'howl'],
	'Salamence': ['dragondance', 'hydropump'],
	'Pikachu': ['teeterdance', 'yawn', 'sing', 'extremespeed', 'lastresort'],
	'Meowth': ['sing'],
	'Suicune': ['sheercold','aquaring','extremespeed','airslash'],
	'Mewtwo': ['electroball'],
	'Jirachi': ['dracometeor'],
	'Piplup': ['sing'],
	'Victini': ['fusionflare','boltstrike','glaciate','vcreate','blueflare','fusionbolt'],
	'Arceus': ['roaroftime','spacialrend','shadowforce'],
	'Snivy': ['aromatherapy'],
	'Zekrom': ['haze'],
	'Rayquaza': ['vcreate'],
	'Raikou': ['extremespeed','aurasphere','weatherball','zapcannon'],
	'Pichu': ['endeavor'],
	'Darkrai': ['spacialrend','roaroftime'],
	'Reshiram': ['mist'],
	'Audino': ['present']}

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
	if poke['species'] in cherishonly:
		ball = 'cherish'
		nonick = True
		#print poke['species']+' is cherish-only'
	for move in poke['moves']:
		if move in movepool[keyify(poke['species'])]:
			if poke['species'] in cherishmove:
				if move in cherishmove[poke['species']]:
					ball = 'cherish'
					nonick = True
					#print move+' is event-only on '+poke['species']
		else:
			ball = 'cherish'
			#print move+' is illegal on '+poke['species']
			break

	if ball == 'pokeball':
		if poke['species'] in dreamradar:
			if poke['ability'] == dreamradar[poke['species']]:
				ball = 'dream'
	return [ball,nonick]
