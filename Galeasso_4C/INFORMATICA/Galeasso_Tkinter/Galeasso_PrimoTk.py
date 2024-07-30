#GALEASSO FEDERICO 4C 9/3/2023 PRIMO ES TKINTER

#Per verificare se la tkinter è installata --> python3 -m tkinter
#import della tkinter (con alias --> import tkinter as tk)
import tkinter

import os
def clearScreen():
	os.system("clear")
clearScreen()

#Creazione della finestra, eredita dal padre (tkinter) tutti i metodi
class Finestra(tkinter.Tk):
	def __init__(self, nome):
		super().__init__()
		
		#Nome della finestra
		self.title("Finestra Grafica " + nome)
		
		#Dimensione della finestra
		self.geometry("300x200")
		
		#Ridimensionamento della finestra:
		#	0,0 --> no ridimensionamento
		#	1,0 --> ridimensionamento oriz
		#	0,1 --> ridimensionamento vert
		#	1,1 --> ridimensionamento oriz e vert
		self.resizable(0,0)
		
		#Widget
		self.crea_widgets()
		
	def crea_widgets(self):
		#Creazione del frame
		mf=tkinter.Frame(self)
		
		#Tipo di layout --> grid (funziona per righe/colonne)
		mf.grid()
		
		#Creazione Lable
		lbl1=tkinter.Label(mf, text="Premi il pulsante --> ")
		
		#Inserimento del label all'interno del frame
		lbl1.grid(row=0, column=0)
		
		#Creazione Button
		btn1=tkinter.Button(mf, text="Sono il pulsante")
		
		#Inserimento del button all'interno del frame
		btn1.grid(row=0, column=1)
			
# main()
def main():
	f=Finestra("Main")
	f.mainloop()
main()
