#!/usr/bin/env python3

import tkinter
import random
from functools import partial


class Finestra(tkinter.Tk):

	def __init__(self):
		super().__init__()
		self.option_add("*Font", "arial 16 bold")
		self.title("Campo Minato")
		#self.geometry("1140x700")
		self.resizable(0,0)
		self.config(bg="cyan")
		self.crea_widgets()
	
	def crea_widgets(self):
		self.frmTabellone=tkinter.Frame()
		self.frmTabellone.grid(row=0, column=0)
		self.lb1=tkinter.Label(self.frmTabellone, text="Punti:", width=10, anchor=tkinter.E)
		self.lb1.grid(row=0, column=0)
		self.lblpt=tkinter.Label(self.frmTabellone, text="0", width=10, anchor=tkinter.W)
		self.lblpt.grid(row=0, column=1)

		self.lstMine=[]
		self.frmCampo=tkinter.Frame()
		self.frmCampo.grid(row=1, column=0)
		self.dizBt={}
		for i in range(10):
			for j in range(10):
				self.dizBt[(i,j)]=tkinter.Button(self.frmCampo, text="", width=4, command=partial(self.scopriMine,i,j))
				self.dizBt[(i,j)].grid(row=i, column=j)
				if random.randrange(6)==0:
					self.lstMine.append((i,j))		

		self.frmPiede=tkinter.Frame()
		self.frmPiede.grid(row=2, column=0)
		self.btnEsci=tkinter.Button(self.frmPiede, text="ESCI", width=20, command=self.destroy)
		self.btnEsci.grid(row=0, column=0)

	def scopriMine(self,riga,colonna):
		if (riga,colonna) in self.lstMine:
			self.haiPerso(riga,colonna)
		elif self.dizBt[(riga,colonna)]["bg"]=="white":
			print("Se riscopri celle già scoperte perdi 1 punto!")
			self.dizBt[(riga, colonna)].config(text="O", bg="blue", fg="yellow")
			self.lblpt["text"] = str(int(self.lblpt["text"]) - 1)
		else:
			self.lblpt["text"] = str(int(self.lblpt["text"]) + 1)
			self.sbiancaContorno(riga,colonna)

	def sbiancaContorno(self,riga,colonna):
		for i in range(colonna - 1, colonna + 2):
			self.dizBt.get((riga, i), tkinter.Button(self.frmCampo)).config(bg="white")
			self.dizBt.get((riga - 1, i), tkinter.Button(self.frmCampo)).config(bg="white")
			self.dizBt.get((riga + 1, i), tkinter.Button(self.frmCampo)).config(bg="white")

	def haiPerso(self,riga,colonna):
		print("Hai perso!")
		for child in self.frmCampo.winfo_children():
			child.configure(state='disable')
		self.dizBt[(riga, colonna)].config(text="X", bg="red", fg="yellow")
		self.lblpt.config(bg = "green", fg = "white")
		self.lb1.config(bg = "green", fg = "white")
		self.frmRigioca=tkinter.Frame()
		self.frmRigioca.grid(row=1, column=0)
		self.btnRigioca=tkinter.Button(self.frmRigioca, bg="purple", fg="white", text="Rigioca", width=20, command=self.rigioca)
		self.btnRigioca.grid(row=0, column=0)

	def rigioca(self):
		self.frmTabellone.destroy()
		self.frmCampo.destroy()
		self.frmPiede.destroy()
		self.frmRigioca.destroy()
		self.crea_widgets()


def main():
	f=Finestra()
	tkinter.mainloop()

main()
