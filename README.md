sim2pkm
=======

A project for taking PO/PS exports and converting them to pkm files for easy importing into Pokegen. Also supports input in the form of PS-style JSON.

Pokemon created by sim2pkm are not designed to pass hack checks, but sim2pkm *does* do a bit of work to try to make sets look legal: for starters, if a Pokemon is only legally obtained inside a Cherish Ball (event) or Dream Ball (dream radar), it will be put in said ball. If the set is illegal (as in, the Pokemon doesn't learn said move at all--sim2pkm does not yet check for illegal combos), it's also put in a Cherish Ball. In addition, if the Pokemon has a move that is only obtainable from an event, where it can't be nicknamed (or the nickname is greater than 10 characters long), sim2pkm will remove the nickname. Finally, sim2pkm will force Pokemon to be shiny or not if the Pokemon's moveset requires it (example: Extremespeed Entei).

Note that sim2pkm does not bother with legal PIDs.

This program can be used from the command-line, but I imagine most people will want to use the GUI interface provided by the gui.py file.

Below is an example script showing how one might use this. Assume you've taken a team in PS, exported it, and saved it as "test.txt" and that you've created a subfolder for your pkm files called "pkms"

```python
import sim2pkm

file=open("test.txt")
test=file.readlines()
splitraw=sim2pkm.splitExport(test)
pokes = []
for entry in splitraw:
	pokes.append(sim2pkm.sim2poke(entry))
for poke in pokes:
	sim2pkm.writepkm('pkms/'+poke['species']+'.pkm',poke)
```
