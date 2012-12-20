# Based on tkinterEntryWidget.py
# by S.Prasanna
from Tkinter import *
import sim2pkm
import tkMessageBox
from tkFileDialog import askdirectory

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
	raw= entryWidget.get().split('\n')
	for i in range(len(raw)):
		raw[i]=raw[i]+'\n'

	splitraw=sim2pkm.splitExport(raw)
	pokes = []
	for entry in splitraw:
		pokes.append(sim2pkm.sim2poke(entry))
	for poke in pokes:
		sim2pkm.writepkm(dirname+'/'+poke['species']+'.pkm',poke)
    	root.destroy()

dirname = '..'
root = Tk()
root.withdraw()

root.title("sim2pkm")

# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root)
w = Label(root, text="Paste your PO/PS export below:")
w.pack()

# Create an Entry Widget in textFrame
entryWidget = mywidgets(textFrame)

textFrame.pack()

button = Button(textFrame, text="Generate pkms & close", command=doTheThing)
button.pack() 
dirname = askdirectory(parent=root, initialdir='.', title='Select folder to generate pkm files into')
root.deiconify()
root.mainloop()
