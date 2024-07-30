#GALEASSO FEDERICO 4C 15/3/2023 COMPITO CALCOLATRICE TKINTER

#Per verificare se la tkinter è installata --> python3 -m tkinter
#import della tkinter (con alias --> import tkinter as tk)
import tkinter

#import delle finestre di dialogo
from tkinter import messagebox

import os
def clearScreen():
	os.system("clear")
clearScreen()

#Creazione della finestra, eredita dal padre (tkinter) tutti i metodi
class Finestra(tkinter.Tk):
	def __init__(self, nome):
		super().__init__()
		
		#Nome della finestra
		self.title(nome)
		
		#Dimensione della finestra
		self.geometry("350x250")
		
		#Ridimensionamento della finestra:
		#	0,0 --> no ridimensionamento
		#	1,0 --> ridimensionamento oriz
		#	0,1 --> ridimensionamento vert
		#	1,1 --> ridimensionamento oriz e vert
		self.resizable(1,1)
		
		#Widget
		self.crea_widgets()
		
	def crea_widgets(self):
		#Creazione del frame
		mf=tkinter.Frame(self)
		
		#Tipo di layout --> grid (funziona per righe/colonne)
		mf.grid()
		
		#Numero 1
		lbl_n1=tkinter.Label(mf, text="Numero 1")
		lbl_n1.grid(row=0, column=0)
		n1=tkinter.DoubleVar()
		entry_n1=tkinter.Entry(mf, textvariable=n1)
		entry_n1.grid(row=0, column=1)
		
		#Numero 2
		lbl_n2=tkinter.Label(mf, text="Numero 2")
		lbl_n2.grid(row=1, column=0)
		n2=tkinter.DoubleVar()
		entry_n2=tkinter.Entry(mf, textvariable=n2)
		entry_n2.grid(row=1, column=1)
		
		#Calcolo e stampa della somma
		def stampaSomma():				
			lbl_somma=tkinter.Label(mf, text="Risultato")
			lbl_somma.grid(row=5, column=0)
			somma=tkinter.DoubleVar()
			entry_somma=tkinter.Entry(mf, textvariable=somma)
			entry_somma.grid(row=5, column=1)
			
			n1_get=n1.get()
			n2_get=n2.get()
			somma_set=n1_get+n2_get
			somma.set(somma_set)
			
		#Button somma
		btn_somma=tkinter.Button(mf, text="+", command=stampaSomma)
		btn_somma.grid(row=3, column=1)
		
		#Calcolo e stampa della sottrazione
		def stampaSot():		
			lbl_sot=tkinter.Label(mf, text="Risultato")
			lbl_sot.grid(row=5, column=0)
			sot=tkinter.DoubleVar()
			entry_sot=tkinter.Entry(mf, textvariable=sot)
			entry_sot.grid(row=5, column=1)
			
			n1_get=n1.get()
			n2_get=n2.get()
			sot_set=n1_get-n2_get
			sot.set(sot_set)
		
		#Button sottrazione
		btn_sot=tkinter.Button(mf, text="-", command=stampaSot)
		btn_sot.grid(row=3, column=2)
		
		#Calcolo e stampa della moltiplicazione
		def stampaMolt():		
			lbl_molt=tkinter.Label(mf, text="Risultato")
			lbl_molt.grid(row=5, column=0)
			molt=tkinter.DoubleVar()
			entry_molt=tkinter.Entry(mf, textvariable=molt)
			entry_molt.grid(row=5, column=1)
			
			n1_get=n1.get()
			n2_get=n2.get()
			molt_set=n1_get*n2_get
			molt.set(molt_set)
		
		#Button moltiplicazione
		btn_molt=tkinter.Button(mf, text="*", command=stampaMolt)
		btn_molt.grid(row=4, column=1)
		
		#Calcolo e stampa della divisione
		def stampaDiv():				
			n1_get=n1.get()
			n2_get=n2.get()
			if n2_get!=0:
				lbl_div=tkinter.Label(mf, text="Risultato")
				lbl_div.grid(row=5, column=0)
				div=tkinter.DoubleVar()
				entry_div=tkinter.Entry(mf, textvariable=div)
				
				entry_div.grid(row=5, column=1)
				div_set=n1_get/n2_get
				div.set(div_set)
			else:
				 messagebox.showerror("Errore", "Il divisore non può essere 0")
		
		#Button divisione
		btn_div=tkinter.Button(mf, text="/", command=stampaDiv)
		btn_div.grid(row=4, column=2)
		
		#Button esci
		btn_esci=tkinter.Button(mf, text="Esci", command=mf.destroy)
		btn_esci.grid(row=7, column=0)
			
# main()
def main():
	f=Finestra("Calcolatrice - Galeasso")
	f.mainloop()
main()
