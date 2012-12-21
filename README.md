sim2pkm
=======

A project for taking PO/PS exports and converting them to pkm files for easy importing into Pokegen. Also supports input in the form of PS-style JSON.

Supports ball enforcement (Pokeball is default. Cherish is forced for event-only/illegal movesets. Dream Ball is forced when ability demands it (dream radar)), nicknames and hidden power IVs.

gui.py provides a rudimentary GUI interface, or one can use it from the command-line, as in the example below.

Here's an example script showing how one might use this. Assume you've taken a team in PS, exported it, and saved it as "test.txt" and that you've created a subfolder for your pkm files called "pkms"

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
