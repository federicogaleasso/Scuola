#GALEASSO FEDERICO 4C 9/3/2023 SECONDO ES TKINTER

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
		
		#Nome
		lbl1=tkinter.Label(mf, text="Nome: ")
		lbl1.grid(row=0, column=0)
		entry=tkinter.Entry(mf)
		entry.grid(row=0, column=1)
		
		#Cognome
		lbl2=tkinter.Label(mf, text="Cognome: ")
		lbl2.grid(row=1, column=0)
		entry2=tkinter.Entry(mf)
		entry2.grid(row=1, column=1)
		
		#Sesso
		lbl3=tkinter.Label(mf, text="Sesso:")
		lbl3.grid(row=2, column=0)
		radiobutton1 = tkinter.Radiobutton(mf, text="Maschio", value="Opzione 1")
		radiobutton1.grid(row=2, column=1)
		radiobutton2 = tkinter.Radiobutton(mf, text="Femmina", value="Opzione 2")
		radiobutton2.grid(row=2, column=2)
		
		#Cibo preferito
		lbl4=tkinter.Label(mf, text="Cibo preferito:")
		lbl4.grid(row=3, column=0)
		checkbutton1 = tkinter.Checkbutton(mf, text="Pizza")
		checkbutton1.grid(row=3, column=1)
		checkbutton2 = tkinter.Checkbutton(mf, text="Sushi")
		checkbutton2.grid(row=3, column=2)
		
		#Paese
		var = tkinter.StringVar(value="Paese")
		menu = tkinter.OptionMenu(mf, var, "Italia", "America", "Germania", "Spagna", "Francia")
		menu.grid(row=4, column=0)
		
		#Invia
		btn1=tkinter.Button(mf, text="Invia")
		btn1.grid(row=5, column=1)
			
# main()
def main():
	f=Finestra("Main")
	f.mainloop()
main()
