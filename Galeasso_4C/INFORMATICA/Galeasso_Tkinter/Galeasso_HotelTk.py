#GALEASSO FEDERICO 24/3/2023 COMPITO - HOTEL TKINTER

#Per verificare se la tkinter è installata --> python3 -m tkinter
#import della tkinter (con alias --> import tkinter as tk)
import tkinter

#import delle finestre di dialogo
from tkinter import messagebox

#impostazioni di localizazione
import locale
locale.setlocale(locale.LC_ALL, '')

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
		self.geometry("500x430")
		
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
		
		#Font
		mf.option_add("*Label.Font", "arial 15")
		mf.option_add("*Radiobutton.Font", "arial 15")
		mf.option_add("*Checkbutton.Font", "arial 15")
		mf.option_add("*Button.Font", "arial 13")
		
		#Tipo di layout --> grid (funziona per righe/colonne)
		mf.grid()
		
		#Titolo
		lbl_titolo=tkinter.Label(mf, text="Hotel Bellavista", font=("arial", 15, "bold"))
		lbl_titolo.grid(row=0, column=1, pady=10, padx=10)
		
		#Cognome
		lbl_cognome=tkinter.Label(mf, text="Cognome")
		lbl_cognome.grid(row=1, column=0, sticky="w", pady=10, padx=20)
		cognome=tkinter.StringVar()
		entry_cognome=tkinter.Entry(mf, textvariable=cognome)
		entry_cognome.grid(row=1, column=1, pady=10, ipady=5)
		
		#Nome
		lbl_nome=tkinter.Label(mf, text="Nome")
		lbl_nome.grid(row=2, column=0, sticky="w", pady=10, padx=20)
		nome=tkinter.StringVar()
		entry_nome=tkinter.Entry(mf, textvariable=nome)
		entry_nome.grid(row=2, column=1, pady=10, ipady=5)
		
		#Tipo di stanza
		lbl3=tkinter.Label(mf, text="Tipo di stanza")
		lbl3.grid(row=3, column=0, sticky="w", pady=(10,0), padx=20)
		opzione_rdo=tkinter.StringVar()
		radiobutton1 = tkinter.Radiobutton(mf, text="Singola", value="Singola", variable=opzione_rdo)
		radiobutton1.grid(row=4, column=0, sticky="w", padx=10)
		radiobutton2 = tkinter.Radiobutton(mf, text="Matrimoniale", value="Matrimoniale", variable=opzione_rdo)
		radiobutton2.grid(row=4, column=1, sticky="w")
		
		#Numero notti
		lbl_nNot=tkinter.Label(mf, text="N. Notti:")
		lbl_nNot.grid(row=5, column=0, sticky="w", pady=10, padx=20)
		nNot=tkinter.IntVar()
		entry_nNot=tkinter.Entry(mf, textvariable=nNot)
		entry_nNot.grid(row=5, column=1, pady=10, ipady=5)
		
		#Servizi extra
		lbl4=tkinter.Label(mf, text="Servizi extra")
		lbl4.grid(row=6, column=0, sticky="w", pady=(10,0), padx=20)
		opzione_1=tkinter.IntVar()
		checkbutton1 = tkinter.Checkbutton(mf, text="Piscina", variable=opzione_1)
		checkbutton1.grid(row=7, column=0, sticky="w", padx=10)
		opzione_2=tkinter.IntVar()
		checkbutton2 = tkinter.Checkbutton(mf, text="Parcheggio", variable=opzione_2)
		checkbutton2.grid(row=7, column=1, sticky="w")
		opzione_3=tkinter.IntVar()
		checkbutton3 = tkinter.Checkbutton(mf, text="Wi-Fi", variable=opzione_3)
		checkbutton3.grid(row=7, column=2, sticky="w")
		
		#funzione prenota()
		def prenota():
			nome_val = nome.get()
			cognome_val = cognome.get()
			nNot_val = nNot.get()
			opzione_rdo_val = opzione_rdo.get()
			opzione_1_val = opzione_1.get()
			opzione_2_val = opzione_2.get()
			opzione_3_val = opzione_3.get()
			
			servizi_extra = []
			if opzione_1_val:
			  servizi_extra.append("Piscina")
			if opzione_2_val:
			  servizi_extra.append("Parcheggio")
			if opzione_3_val:
			  servizi_extra.append("Wi-Fi")
			
			messagebox.showinfo("Riepilogo Prenotazione", "Prenotazione effettuata!\n\nIl sig. \"{}\" \"{}\"\n\nha prenotato una stanza \"{}\" per \"{}\" notte/i\n\ncon i seguenti servizi extra: {}".format(cognome_val, nome_val, opzione_rdo_val, nNot_val, servizi_extra))
			
			with open("riepilogo_prenotazione.txt", "w") as file:
				file.write("Riepilogo Prenotazione\n\nIl sig. \"{}\" \"{}\"\n\nha prenotato una stanza \"{}\" per \"{}\" notte/i\n\ncon i seguenti servizi extra: {}".format(cognome_val, nome_val, opzione_rdo_val, nNot_val, servizi_extra))

		
		#Button prenota
		btn_calcola=tkinter.Button(mf, text="PRENOTA", command=prenota)
		btn_calcola.grid(row=8, column=1, sticky="ew", columnspan=1, pady=10, padx=10)
		
# main()
def main():
	f=Finestra("Hotel - Galeasso")
	f.mainloop()
main()
