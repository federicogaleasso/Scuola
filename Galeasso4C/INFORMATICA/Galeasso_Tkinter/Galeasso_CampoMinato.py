#GALEASSO FEDERICO 31/3/2023 COMPITO - CAMPO MINATO

import tkinter
import random
from functools import partial

import os
def clearScreen():
	os.system("clear")
clearScreen()

class Finestra(tkinter.Tk):
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.resizable(0,0)
		self.crea_widgets()
		self.config(bg="cyan")
		self.punteggio=0
		
	def crea_widgets(self):
		#Frame punti
		self.punteggio=0
		frame_punti=tkinter.Frame(self)
		frame_punti.grid(row=0, column=0)
		lbl1_punti=tkinter.Label(frame_punti, text="Punti:", font=("TkDefaultFont", 14, "bold"))
		lbl1_punti.grid(row=0, column=0, ipadx=50)
		lbl2_punti=tkinter.Label(frame_punti, text="0", font=("TkDefaultFont", 14, "bold"))
		lbl2_punti.grid(row=0, column=1, ipadx=50)
		
		def click_mina(i,j):
			if (i,j) in mine:
				gameover(i,j)
				lbl1_punti.config(bg="green", fg="white")
				lbl2_punti.config(bg="green", fg="white")
			if campo[(i, j)]['bg'] == "white":
				campo[(i,j)].config(bg="blue", fg="yellow", text="O")
				self.punteggio -= 1
				lbl2_punti.config(text=str(self.punteggio))
			else:
				for x in range(i-1, i+2):
					for y in range(j-1, j+2):
						campo[(x,y)].config(bg="white")
				self.punteggio += 1
				lbl2_punti.config(text=str(self.punteggio))
		
		def rigioca():
			frame_punti.destroy()
			frame_campo.destroy()
			frame_esci.destroy()
			self.frame_rigioca.destroy()
			self.crea_widgets()
				
		def gameover(i,j):
			campo[(i,j)].config(bg="red", fg="yellow", text="X")
			self.frame_rigioca=tkinter.Frame()
			self.frame_rigioca.grid(row=1, column=0)
			btn_rigioca=tkinter.Button(self.frame_rigioca, bg="purple", fg="white", text="Rigioca", width=20, font=("TkDefaultFont", 14, "bold"), command=rigioca)
			btn_rigioca.grid(row=0, column=0)
			for button in campo.values():
				button.config(state="disabled")
		
		#Frame campo
		mine=[]
		campo={}
		frame_campo=tkinter.Frame(self)
		frame_campo.grid()
		for i in range(10):
			for j in range(10):
				campo[(i,j)]=tkinter.Button(frame_campo, text="", width=4, command=partial(click_mina,i,j))
				campo[(i,j)].grid(row=i, column=j)
				mine.append((0,0))
				mine.append((2,5))
				mine.append((5,1))
				mine.append((9,9))
				mine.append((6,7))
		
		#Frame esci
		frame_esci=tkinter.Frame(self)
		frame_esci.grid()
		btn_esci=tkinter.Button(frame_esci, text="ESCI", font=("TkDefaultFont", 14, "bold"), command=self.destroy)
		btn_esci.grid(row=0, column=0, ipadx=100)
		
# main()
def main():
	f=Finestra("Campo Minato - Galeasso")
	f.mainloop()
main()
