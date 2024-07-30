#GALEASSO FEDERICO 23/3/2023 COMPITO - ALBERGO TKINTER (aggiunta MODULO LOCALE)

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
		self.geometry("650x560")
		
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
		
		#Titolo
		lbl_titolo=tkinter.Label(mf, text="Prenotazione Alberghiera", font=("TkDefaultFont", 14, "bold"))
		lbl_titolo.grid(row=0, column=0, sticky="ew", columnspan=4, pady=10)
		
		#Nome
		lbl_nome=tkinter.Label(mf, text="Nome Prenotazione")
		lbl_nome.grid(row=1, column=0, sticky="w", pady=10)
		nome=tkinter.StringVar()
		entry_nome=tkinter.Entry(mf, textvariable=nome)
		entry_nome.grid(row=1, column=1, sticky="ew", columnspan=3, ipady=10, padx=10)
		
		#Cognome
		lbl_cognome=tkinter.Label(mf, text="Cognome Prenotazione")
		lbl_cognome.grid(row=2, column=0, sticky="w", pady=10)
		cognome=tkinter.StringVar()
		entry_cognome=tkinter.Entry(mf, textvariable=cognome)
		entry_cognome.grid(row=2, column=1, sticky="ew", columnspan=3, ipady=10, padx=10)
		
		#Numero totale di persone
		lbl_nTotPers=tkinter.Label(mf, text="Numero totale persone")
		lbl_nTotPers.grid(row=3, column=0, sticky="we" + "ns", rowspan=2)
		nTotPers=tkinter.IntVar()
		entry_nTotPers=tkinter.Entry(mf, textvariable=nTotPers)
		entry_nTotPers.grid(row=3, column=1, sticky="ns", rowspan=2, pady=10, padx=10)
		
		#Numero adulti
		lbl_nAdu=tkinter.Label(mf, text="Numero adulti")
		lbl_nAdu.grid(row=3, column=2, sticky="w")
		nAdu=tkinter.IntVar()
		entry_nAdu=tkinter.Entry(mf, textvariable=nAdu)
		entry_nAdu.grid(row=3, column=3, pady=10, ipady=10, padx=10)
		
		#Numero bambini
		lbl_nBam=tkinter.Label(mf, text="Numero bambini")
		lbl_nBam.grid(row=4, column=2, sticky="w")
		nBam=tkinter.IntVar()
		entry_nBam=tkinter.Entry(mf, textvariable=nBam)
		entry_nBam.grid(row=4, column=3, pady=10, ipady=10, padx=10)
		
		#Numero notti
		lbl_nNot=tkinter.Label(mf, text="Numero notti")
		lbl_nNot.grid(row=5, column=1, sticky="w", padx=10)
		nNot=tkinter.IntVar()
		entry_nNot=tkinter.Entry(mf, textvariable=nNot)
		entry_nNot.grid(row=5, column=2, pady=10, ipady=10)
		
		#Numero camere singole
		lbl_nCamSing=tkinter.Label(mf, text="N. Camere Singole")
		lbl_nCamSing.grid(row=6, column=0, sticky="w")
		nCamSing=tkinter.IntVar()
		entry_nCamSing=tkinter.Entry(mf, textvariable=nCamSing)
		entry_nCamSing.grid(row=6, column=1, pady=10, ipady=10)
		
		#Numero camere matrimoniali
		lbl_nCamMat=tkinter.Label(mf, text="N. Camere Matrimoniali")
		lbl_nCamMat.grid(row=6, column=2, sticky="w")
		nCamMat=tkinter.IntVar()
		entry_nCamMat=tkinter.Entry(mf, textvariable=nCamMat)
		entry_nCamMat.grid(row=6, column=3, pady=10, ipady=10)
		
		#Funzione calcola()
		def calcola():
			nTotPers_val=nTotPers.get()
			nAdu_val=nAdu.get()
			nBam_val=nBam.get()
			nNot_val=nNot.get()
			somDaVers_val=somDaVers.get()
			nCamSing_val=nCamSing.get()
			nCamMat_val=nCamMat.get()
			nome_val=nome.get()
			cognome_val=cognome.get()
			
			#Controllo sul campo nome
			if len(nome_val)==0:
				messagebox.showerror("Errore", "Compilare il campo nome")
			
			#Controllo sul campo cognome
			if len(cognome_val)==0:
				messagebox.showerror("Errore", "Compilare il campo cognome")
			
			#Controllo sul campo Numero di Bambini/Adulti
			if int(nAdu_val)<1 and int(nBam_val)<1:
				messagebox.showerror("Errore", "Devi prenotare almeno per una persona")
			
			#Controllo sul campo Camere Singole/Matrimoniali
			if int(nCamSing_val)<1 and int(nCamMat_val)<1:
				messagebox.showerror("Errore", "Devi prenotare almeno una delle due camere")
			
			#Controllo sul Numero totale di persone
			if nTotPers_val != (nAdu_val+nBam_val):
				messagebox.showerror("Errore", "Il numero di persone totali non è corretto")
				entry_nTotPers.configure(bg="red")
				entry_nTotPers.delete(0,tkinter.END)
				entry_nAdu.delete(0,tkinter.END)
				entry_nBam.delete(0,tkinter.END)
				entry_nTotPers.insert(0,"0")
				entry_nAdu.insert(0,"0")
				entry_nBam.insert(0,"0")
			else:
				entry_nTotPers.configure(bg="white")
			
			#Controllo sul numero di notti
			if nNot_val <= 0:
				messagebox.showerror("Errore", "Il numero di notti deve essere maggiore di zero")
				entry_nNot.configure(bg="red")
				entry_nNot.delete(0,tkinter.END)
				entry_nNot.insert(0,"0")
			else:
				entry_nNot.configure(bg="white")
			
			#Controllo per eseguire la somma
			if nTotPers_val == (nAdu_val+nBam_val) and nNot_val > 0 and len(nome_val)>0 and len(cognome_val)>0 and (int(nAdu_val)>0 or int(nBam_val)>0) and int(nCamSing_val)>0 or int(nCamMat_val)>0:
				somDaVers_val=((nCamSing_val*80)*nNot_val)+((nCamMat_val*150)*nNot_val)
				somDaVers.set(somDaVers_val)

				somDaVers_formatted.set(locale.currency(somDaVers.get()))
				
				if somDaVers_val > 300:
					entry_somDaVers.configure(fg="blue")
				else:
					entry_somDaVers.configure(fg="green")
				messagebox.showinfo("Riepilogo", "Prenotazione effettuata!\nNome: {}\nCognome: {}\nPersone totali: {}\nAdulti: {}\nBambini: {}\nNotti: {}\nCamere singole: {}\nCamere matrimoniali: {}".format(nome_val, cognome_val, nTotPers_val, nAdu_val, nBam_val, nNot_val, nCamSing_val, nCamMat_val))
				
		#Funzione annulla()
		def annulla():
			
			entry_nTotPers.delete(0,tkinter.END)
			entry_nAdu.delete(0,tkinter.END)
			entry_nBam.delete(0,tkinter.END)
			entry_nNot.delete(0,tkinter.END)
			entry_nCamSing.delete(0,tkinter.END)
			entry_nCamMat.delete(0,tkinter.END)
			entry_nome.delete(0,tkinter.END)
			entry_cognome.delete(0,tkinter.END)
			
			entry_nTotPers.insert(0,"0")
			entry_nAdu.insert(0,"0")
			entry_nBam.insert(0,"0")
			entry_nNot.insert(0,"0")
			entry_nCamSing.insert(0,"0")
			entry_nCamMat.insert(0,"0")
			entry_nome.insert(0,"")
			entry_cognome.insert(0,"")
			
			entry_somDaVers.configure(state="normal")
			entry_somDaVers.delete(0,tkinter.END)
			entry_somDaVers.configure(fg="black")
			entry_somDaVers.configure(state="readonly")
			
			entry_nTotPers.configure(bg="white")
			entry_nNot.configure(bg="white")
		
		#Button calcola
		btn_calcola=tkinter.Button(mf, text="CALCOLA", command=calcola)
		btn_calcola.grid(row=7, column=1, sticky="ew", columnspan=1, pady=10, padx=10)
		
		#Button annulla
		btn_annulla=tkinter.Button(mf, text="ANNULLA", command=annulla)
		btn_annulla.grid(row=7, column=2, sticky="ew", columnspan=1, pady=10)
		
		#Somma da versare
		lbl_somDaVers=tkinter.Label(mf, text="Somma da versare")
		lbl_somDaVers.grid(row=8, column=0, sticky="we" + "ns")
		somDaVers=tkinter.DoubleVar()
		somDaVers_formatted=tkinter.StringVar()
		entry_somDaVers=tkinter.Entry(mf, textvariable=somDaVers_formatted, state='readonly')
		entry_somDaVers.grid(row=8, column=1, sticky="ew", columnspan=3, pady=10, ipady=15, padx=10)

		#Button esci
		btn_esci=tkinter.Button(mf, text="ESCI", command=self.destroy)
		btn_esci.grid(row=9, column=3, sticky="ew", columnspan=1, pady=10, padx=10)

# main()
def main():
	f=Finestra("Albergo - Galeasso")
	f.mainloop()
main()
