#!/usr/bin/python
# Based on tkinterEntryWidget.py
# by S.Prasanna
from Tkinter import *
import sim2pkm
import tkMessageBox
from tkFileDialog import askdirectory
import json
import webbrowser

class mywidgets:
	def __init__(self,root):
		frame=Frame(root)
		frame.pack()
		self.txtfr(frame)
		return

	def txtfr(self,frame):
		
		#define a new frame and put a text area in it
		textfr=Frame(frame)
		self.text=Text(textfr,height=20,width=80,background='white')
		
		# put a scroll bar in the frame
		scroll=Scrollbar(textfr)
		self.text.configure(yscrollcommand=scroll.set)
		
		#pack everything
		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT,fill=Y)
		textfr.pack(side=TOP)
		return

	def get(self):
		return self.text.get('0.0',END)


def doTheThing():
	global entryWidget
	pokes = []
	raw= entryWidget.get().split('\n')
	if raw[0].startswith('[{"'):
		team = json.loads(raw[0])
		for entry in team:
			pokes.append(sim2pkm.json2poke(entry))
	else:
		for i in range(len(raw)):
			raw[i]=raw[i]+'\n'
		splitraw=sim2pkm.splitExport(raw)
		for entry in splitraw:
			pokes.append(sim2pkm.sim2poke(entry))
	for i in range(len(pokes)):
		if randTeam.get():
			filename = str(i+1)
		else:
			filename = pokes[i]['species']
		sim2pkm.writepkm(dirname+'/'+filename+'.pkm',pokes[i])
    	root.destroy()

def randbats():
	webbrowser.open("http://koalus-et-arbor.dyndns-ip.com/cgi-bin/randbats.sh")
def challengecup():
	webbrowser.open("http://koalus-et-arbor.dyndns-ip.com/cgi-bin/CC.sh")

dirname = '..'
root = Tk()
randTeam = IntVar()
root.withdraw()

root.title("sim2pkm")

# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root)
w = Label(root, text="Paste your team below:")
w.pack()

# Create an Entry Widget in textFrame
entryWidget = mywidgets(textFrame)

textFrame.pack()

button = Button(textFrame, text="Generate pkms & close", command=doTheThing)
button.pack(side=LEFT)

randbats = Button(textFrame, text="Get a randbats team", command=randbats)
randbats.pack(side=LEFT)

CC = Button(textFrame, text="Get a Challenge Cup team", command=challengecup)
CC.pack(side=LEFT)

c = Checkbutton(textFrame, text="Numbered pkms", variable=randTeam)
c.pack(side=RIGHT)
dirname = askdirectory(parent=root, initialdir='.', title='Select folder to generate pkm files into')
root.deiconify()
root.mainloop()
