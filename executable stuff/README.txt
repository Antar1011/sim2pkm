Thank you for downloading sim2pkm

v1.5

Project Home: https://github.com/Antar1011/sim2pkm


What is sim2pkm?
	sim2pkm is a simple program for taking PO/PS exports and converting them to pkm files for easy importing into Pokegen. It also
supports input in the form of PS-style JSON strings. While sim2pkm Pokemon are not designed to pass hack
checks, the program does perform some rudimentary "legalizing:" specifically, Pokemon that MUST be in a
given type of Pokeball will be put in that Pokeball, Pokemon that MUST be shiny will be made shiny (and
those that cannot will be forced to not be shiny), and Pokemon that cannot be nicknamed or have a nickname
longer than 10 characters in length will have their nicknames removed.
	The interface also provides links to random team generators, so you can use it to generate pkm files
for Challenge Cup (CC4Wifi) battles as well as Pokemon Showdown-style "randbats."


Instructions:
	-Unzip the entire contents of this archive to some place that's convenient for you.
	-Double-click on and run:
		-WINDOWS: sim2pkm.bat
		-MAC: sim2pkm.command
		-LINUX: sim2pkm.sh
	-A dialog box should first appear that asks you where you want to save your pkm files. The default
is the folder where you unzipped sim2pkm, but you can choose anywhere. You might even want to make yourself
a separate folder somewhere.
	-A window should pop up with a big white area for you to paste your team into. This team can be in
the form of a Pokemon Online importable (go into the teambuilder and go to Team > Export Team), a Pokemon
Showdown importable (go into the teambuilder, select your team and click edit, then click Import/Export),
or a Pokemon Showdown JSON string (the format used by the random team generators--see below).
	-You can also click one of the two center buttons on the bottom of the window to generate a random
team (either randbats or Challenge Cup). These buttons will open a browser tab or window containing an ugly
looking string. Don't worry about it being ugly--just copy it from the browser and paste it into the window.
	-By default, sim2pkm will name the pkm files by the Pokemon species names. You can choose to click
the "Numbered pkms" box which will instead name the pkm files with numbers based on the order in the paste.
You'll pretty much need to use this option if you've got two of the same Pokemon on a team, and it should
also be useful for preserving the random order for random teams.
	-When you're ready, click the "Generate pkms & close" button, and sim2pkm will close. In the folder
you designated, you should now find your pkm files, ready to be imported into Pokegen (Pokesav works fine
as long as you're not doing any BW2 stuff).


Known Issues:
	-This is a Pokegen issue, I'm pretty sure: Shaymin-Sky will revert to its land forme when you load
the game. Just make sure you have a Gracidea flower in your key items, and you can change it back.
	-Right now, you can only paste one team at once (dropping all teams at the same time from PS'
"Backup/Restore" window will end in tears). This should be remedied in a future version.


Having Problems?
	-Send me a PM through Smogon (I'm Antar) or Youtube (I'm Antar1011). I'll be happy to take a look
and try to fix whatever's going on.


Changelog:
v1.5 -- 2013/05/28: Shiny json and Ho-Oh issues fixed
v1.4 -- 2012/12/29: Mac compatibility fix
v1.3 -- 2012/12/24: Pokemon Online compatibility bugfix
v1.2 -- 2012/12/24: Fixed problems with formes
v1.1 -- 2012/12/24: Shiny enforcement and multiple bugfixes 
v1.0 -- 2012/12/21: Released


Credits and License:
	sim2pkm was written by Antar of Smogon (Antar1011 of Youtube). Many thanks go out to Infinite
Recursion for ir-gts-bw, as much of the pkm-generating code for this program was written by reverse
engineering the code from that project. More thanks go out to Zarel, the creator of Pokemon Showdown, for
my random team-generating scripts (as well as most of the data files that this program depends on).

	CC4Wifi is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported
License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a
letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.