from lookup import *
from ballEnforce import *
from random import random

def statFormula(base,lv,nat,iv,ev):
	if nat == -1: #for HP
		return (iv+2*base+ev/4+100)*lv/100+10
	else:
		return ((iv+2*base+ev/4)*lv/100+5)*nat/10

def hpivs(hptype):
	ivs = {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}
	if hptype == 'bug':
		ivs['atk']=30
		ivs['def']=30
		ivs['spd']=30
	#elif hptype == 'dark':
	elif hptype == 'dragon':
		ivs['atk']=30 
	elif hptype == 'electric':
		ivs['spa']=30
	elif hptype == 'fighting':
		ivs['def']=30
		ivs['spa']=30
		ivs['spd']=30
		ivs['spe']=30
	elif hptype == 'fire':
		ivs['atk']=30
		ivs['spa']=30
		ivs['spe']=30
	elif hptype == 'flying':
		ivs['hp']=30
		ivs['atk']=30
		ivs['def']=30
		ivs['spa']=30
		ivs['spd']=30
	elif hptype == 'ghost':
		ivs['def']=30
		ivs['spd']=30
	elif hptype == 'grass':
		ivs['atk']=30
		ivs['spa']=30
	elif hptype == 'ground':
		ivs['spa']=30
		ivs['spd']=30
	elif hptype == 'ice':
		ivs['atk']=30
		ivs['def']=30
	elif hptype == 'poison':
		ivs['def']=30
		ivs['spa']=30
		ivs['spd']=30
	elif hptype == 'psychic':
		ivs['atk']=30
		ivs['spe']=30
	elif hptype == 'rock':
		ivs['def']=30
		ivs['spd']=30
		ivs['spe']=30
	elif hptype == 'steel':
		ivs['spd']=30
	elif hptype == 'water':
		ivs['def']=30
		ivs['spa']=30
	return ivs

def writepkm(filename,poke):
#example:
#poke=	{'species': 'Giratina-Origin',
#	'gender': 'f',
#	'level': 100,
#	'evs': [252,0,252,0,0,4],
#	'ivs': [31,31,31,31,31,31],
#	'moves': ['toxic','rest','surf','icebeam'],
#	'nature': 'Bold',
#	'item': 'Eviolite',
#	'happiness': 255,
#	'ability': 'Levitate'}	

	#forme stuff
	if poke['species'] in formes.keys():
		fakename = formes[poke['species']][0]
		fakenum = formes[poke['species']][1]
		forme = formes[poke['species']][2]
	else:
		fakename = poke['species']
		fakenum = dexno[poke['species']]
		forme = 0
	num = dexno[fakename]

	item = inv_items[poke['item']]
	ability = inv_abilities[poke['ability']]

	[ball, nonick,poke['shiny']] = ballEnforce(poke)
	if nonick:
		poke['nick']=''
	
	if num == 493:
		if item in range(0x012A,0x013A):
			forme = [9,10,12,11,14,1,3,4,2,13,6,5,7,15,16,8][item-0x012A]
		else:
			forme = 0
	if poke == 487:
		if item == 0x0070:
			forme=1
		else:
			forme=0
	if (poke['species']=="Keldeo"):
		if ("secretsword" in poke['moves']):
			forme = 1
		else:
			forme = 0
	if poke['gender'] == 'm':
		gender = 1
	elif poke['gender'] == 'f':
		gender = 2
	else:
		gender=0

	nature = inv_nature[poke['nature']]

	stats=[0]*6
	if poke['species']=='Shedinja':
		stats[0]=1
	else:
		stats[0]=statFormula(pokestats[fakenum][1],poke['level'],-1,poke['ivs'][0],poke['evs'][0])
	stats[1]=statFormula(pokestats[fakenum][2],poke['level'],nmod[nature][1-1],poke['ivs'][1],poke['evs'][1])
	stats[2]=statFormula(pokestats[fakenum][3],poke['level'],nmod[nature][2-1],poke['ivs'][2],poke['evs'][2])
	stats[3]=statFormula(pokestats[fakenum][6],poke['level'],nmod[nature][3-1],poke['ivs'][3],poke['evs'][3])
	stats[4]=statFormula(pokestats[fakenum][4],poke['level'],nmod[nature][4-1],poke['ivs'][4],poke['evs'][4])
	stats[5]=statFormula(pokestats[fakenum][5],poke['level'],nmod[nature][5-1],poke['ivs'][5],poke['evs'][5])

	exp = lvlexp[poke['level']][pokestats[fakenum][0]]

	moves = []
	for move in poke['moves']:
		moves.append(inv_attacks[move])

	#load template sav file
	pkm = open("template.pkm","rb").read()
	p = array('B')
    	p.fromstring(pkm)
	
	#species
	p[0x08]=num%256
	p[0x09]=num/256	

	#gender & forme
	p[0x40]=[0x00,0x08,0x10,0x18,0x20,0x28,0x30,0x38,0x40,0x48,0x50,0x58,0x60,0x68,0x70,0x78,0x80,0x99,0x90,0x98,0xA0,0xA8,0xB0,0xB8,0xC0,0xC8,0xD0,0xD8][forme]
	if gender == 0:
		p[0x40]=p[0x40]+4
	elif gender == 2:
		p[0x40]=p[0x40]+2
	if poke['species']=='Shaymin-Sky':
		p[0x40]=p[0x40]+1 #Shaymin-Sky needs fateful encounter
	#gender must also be set in the PID
	if gender == 1:
		p[0x00]=255
	
	#shiny
	if not poke['shiny']:
		p[0x01]=1

	if poke['shiny'] and gender == 1:
		p[0x02]=p[0x00]	

	#level & exp
	p[0x8c]=poke['level']
	e=exp
	for i in range(16,19):
		p[i]=e%256
		e=e/256

	#ability
	p[0x15] = ability

	#nature
	p[0x41] = nature

	#item
	p[0x0a]=item%256
	p[0x0b]=item/256

	#pokeball
	if ball == 'pokeball':
		p[0x83]=4
	elif ball == 'cherishball':
		p[0x83]=16
	elif ball == 'dreamball':
		p[0x83]=25
	#else:
		#i dunno

	#IVs
	ivcomb=0
	for i in range(0,6):
		ivcomb = ivcomb + (poke['ivs'][i] << 5*i)
	for i in range(56,60):
		p[i]=ivcomb%256
		ivcomb=ivcomb/256
	
	#nicknamed tag
	if poke['nick'] != '':
		p[0x3B]=p[0x3B]+128

	#EVs
	for i in range(0,6):
		p[24+i]=poke['evs'][i]

	#stats
	for i in range(0,6):
		p[144+2*i]=stats[i]%256
		p[145+2*i]=stats[i]/256
	p[142]=p[144]
	p[143]=p[145]

	#happiness
	p[0x14] = poke['happiness']

	#moves
	for i in range(len(moves)):
		p[40+2*i]=moves[i]%256
		p[41+2*i]=moves[i]/256

	#pp
	for i in range(len(moves)):
		p[48+i]=pp[moves[i]]

	#nickname
	if poke['nick'] == '':
		poke['nick']=fakename
	for i in range(len(poke['nick'])):
		p[72+2*i]=ord(poke['nick'][i])
	p[72+2*i+2] = p[72+2*i+3] = p[92] = p[93] = ord('\xff')

	#checksum
	checksum=0
	for i in range(8,137,2):
		checksum = (checksum+p[i]+p[i+1]*256)%65536
	p[0x06]=checksum%256
	p[0x07]=checksum/256

	#write .pkm file
	outfile=open(filename,'wb')
	p.tofile(outfile)
	outfile.close()


def sim2poke(raw):
	species = 'empty'
	nick = ''
	item = 'nothing'
	ability = ''
	level=100
	evs = {'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0}
	ivs = {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}
	moves = []
	gender = 'n'
	happiness = 255
	nature = 'hardy'
	shiny = False

	#first line (species)
	line=raw[0]
	if '(' in line: #nicknamed
		species = keyify(line[string.rfind(line,'(')+1:string.rfind(line,')')])
		nick = line[:string.rfind(line,'(')-1]
		if species in ['m','f']: #you got gender, not species
			gender = species

			if '(' in line[:string.rfind(line,'(')]:
				species = line[string.rfind(line,'(',0,string.rfind(line,'('))+1:string.rfind(line,')',0,string.rfind(line,'('))]
				nick = line[:string.rfind(line,'(',0,string.rfind(line,'('))-1]
			else:
				species = line[:string.rfind(line,'(')]
				nick = species
	else:
		if '@' in line: #is there an item
			species = line[0:string.rfind(line,'@')]
		else:
			species = line[0:len(line)-1]

	if len(nick)>10:
		nick = '' #no nicknames longer than 10 chars

	if species[0] not in string.lowercase + string.uppercase:
		species=species[1:]
	while species[len(species)-1] in ')". ':
		species=species[:len(species)-1]
	if species[0] in string.lowercase or species[1] in string.uppercase:
		species = species.title()
	if species in replacements.keys():
		species = replacements[species]

	for s in aliases: #combine appearance-only variations and weird PS quirks
		if species in aliases[s]:
			species = s
			break
	species = keyify(species)

	if species.startswith('arceus'):
		species = 'arceus'

	if 'gender' in pokedex[species]:
		gender = keyify(pokedex[species]['gender'])
	elif gender == 'n':
		#pick gender at random
		gender = 'f'
		if 'genderRatio' in pokedex[species]:
			if random() < pokedex[species]['genderRatio']['M']:
				gender = 'm'
		else:
			if random < 0.5:
				gender = 'm'

	if '@' in line:
		item = keyify(line[string.rfind(line,'@')+1:len(line)-1])

	for line in raw[1:]:
		if line == '\n':
			break
		
		if line.startswith('Trait:'):
			ability = keyify(line[6:len(line)-1])
		elif line.startswith('Level:'):
			level = int(line[6:len(line)-1])
		elif line.startswith('EVs') or line.startswith('IVs'):
			mods = line[4:len(line)-1].split('/')
			for mod in mods:
				while mod[0] == ' ':
					mod=mod[1:]
				while mod[len(mod)-1] == ' ':
					mod=mod[:len(mod)-1]
				num=mod[:string.find(mod,' ')]
				stat=statTranslate[mod[len(num)+1:]]
				if line.startswith('EVs'):
					evs[stat]=int(num)
				else:
					ivs[stat]=int(num)
		elif line.startswith('Nature'):
			nature = keyify(line[7:string.rfind(line,'(')-1])
		elif line.startswith('Happiness'):
			happiness = int(line[10:len(line)-1])
		elif line[0] == '-':
			move = keyify(line[1:len(line)-1])
			if move.startswith('hiddenpower'):
				if ivs == {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}:
					hptype = move[11:]
					ivs = hpivs(hptype)
				move = 'hiddenpower'
			moves.append(move)
		elif line.startswith('Shiny'):
			if keyify(line[string.find(line,':')+1:]) == 'yes':
				shiny = True
		elif not line.startswith('Shiny'): #nature
			nature = keyify(line[0:string.rfind(line,'ature')-2])#Nature/nature

		
	return {'species': keyLookup[species],
		'nick': nick,
		'gender': gender,
		'level': level,
		'evs': [evs['hp'],evs['atk'],evs['def'],evs['spe'],evs['spa'],evs['spd']],
		'ivs': [ivs['hp'],ivs['atk'],ivs['def'],ivs['spe'],ivs['spa'],ivs['spd']],
		'moves': moves,
		'nature': keyLookup[nature],
		'item': keyLookup[item],
		'happiness': happiness,
		'ability': keyLookup[ability],
		'shiny': shiny}

def json2poke(j):
	species = 'empty'
	nick = ''
	item = 'nothing'
	ability = ''
	level=100
	evs = {'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0}
	ivs = {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}
	moves = []
	gender = 'n'
	happiness = 255
	nature = 'hardy'
	shiny = False

	if 'species' in j:
		species = keyify(j['species'])
	else:
		species = keyify(j['name'])
	if 'item' in j:
		item = keyify(j['item'])
		if keyLookup[item] not in inv_items:
			item = 'nothing'
	if 'ability' in j:
		ability = keyify(j['ability'])
	if 'level' in j:
		level = int(j['level'])
	if 'evs' in j:
		for stat in j['evs']:
			evs[stat]=int(j['evs'][stat])
	if 'ivs' in j:
		for stat in j['ivs']:
			ivs[stat]=int(j['ivs'][stat])
	if 'moves' in j:
		moves = j['moves']
	if 'gender' in j:
		gender = keyify(j['gender'])
	if 'happiness' in j:
		happiness = int(j['happiness'])
	if 'nature' in j:
		nature = keyify(j['nature'])
	if 'shiny' in j:
		shiny = j['shiny']

	for i in range(len(moves)):
		if moves[i].startswith('hiddenpower'):
			if ivs == {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}:
				hptype = moves[i][11:]
				ivs = hpivs(hptype)
			moves[i]='hiddenpower'

	return {'species': keyLookup[species],
		'nick': nick,
		'gender': gender,
		'level': level,
		'evs': [evs['hp'],evs['atk'],evs['def'],evs['spe'],evs['spa'],evs['spd']],
		'ivs': [ivs['hp'],ivs['atk'],ivs['def'],ivs['spe'],ivs['spa'],ivs['spd']],
		'moves': moves,
		'nature': keyLookup[nature],
		'item': keyLookup[item],
		'happiness': happiness,
		'ability': keyLookup[ability],
		'shiny': True}

def splitExport(raw):
	working=[]
	splitraw=[]
	for line in raw:
		if line == '\n':
			if len(working)>1:
				splitraw.append(working)
			working = []
		else:
			working.append(line)
	if len(working)>1:
		splitraw.append(working)
	return splitraw
		
def splitTeams(raw):
	teams={}
	working=[]
	for line in raw:
		if line.startswith('='):
			name = keyify(line)
			teams[name]=[]
		else:
			teams[name].append(line)
	return teams
