#GALEASSO FEDERICO 4C 6/4/2023 RELAZIONE TKINTER - place()

#Il metodo place() consente di posizionare un widget Tkinter in una posizione specifica all'interno del frame o della finestra. È possibile posizionare il widget in modo assoluto o relativo rispetto al frame o alla finestra genitore.

#Sintassi: widget.place(attributi)

#Ecco l'elenco degli attributi:
# x --> specifica la posizione orizzontale in pixel del widget rispetto al lato sinistro del frame o della finestra genitore. Il valore predefinito è 0.

# y -> specifica la posizione verticale in pixel del widget rispetto al lato superiore del frame o della finestra genitore. Il valore predefinito è 0.

# relx --> specifica la posizione orizzontale del widget in modo relativo alla larghezza del frame o della finestra genitore. Il valore predefinito è 0.0, che corrisponde al lato sinistro del frame o della finestra genitore. Il valore di relx è compreso tra 0.0 e 1.0.

# rely --> specifica la posizione verticale del widget in modo relativo all'altezza del frame o della finestra genitore. Il valore predefinito è 0.0, che corrisponde al lato superiore del frame o della finestra genitore. Il valore di rely è compreso tra 0.0 e 1.0.

# relwidth --> specifica la larghezza del widget in modo relativo alla larghezza del frame o della finestra genitore. Il valore predefinito è 0.0, che significa che la larghezza del widget sarà determinata dal contenuto. Il valore di relwidth è compreso tra 0.0 e 1.0.

# relheight --> specifica l'altezza del widget in modo relativo all'altezza del frame o della finestra genitore. Il valore predefinito è 0.0, che significa che l'altezza del widget sarà determinata dal contenuto. Il valore di relheight è compreso tra 0.0 e 1.0.

# width --> specifica la larghezza del widget in pixel. Il valore predefinito è determinato dal contenuto del widget.

# height --> specifica l'altezza del widget in pixel. Il valore predefinito è determinato dal contenuto del widget.

# anchor --> specifica l'ancoraggio del widget rispetto alla sua posizione. Il valore predefinito è "nw" (nord-ovest). Altri valori possibili sono "n" (nord), "ne" (nord-est), "e" (est), "se" (sud-est), "s" (sud), "sw" (sud-ovest), "w" (ovest) e "center" (centro).

# bordermode --> specifica il modo di calcolare la posizione del widget in relazione al bordo della finestra o del frame genitore. Il valore predefinito è "inside" e l'altro valore è 'outside': 'outside' conta x e y dall'angolo in alto a sinistra del frame compreso il bordo, mentre 'inside' lo conta senza il bordo.

import tkinter as tk
from tkinter import messagebox
import os

def clearScreen():
	os.system("clear")
clearScreen()

class Finestra(tk.Tk):
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.resizable(1,1)
		self.crea_widgets()
		
	def crea_widgets(self):
		mf=tk.Frame(self)
		mf.grid()
		mf.config(pady=20)
		
		#Titolo
		lbl_titolo=tk.Label(mf, text="Galeasso - Relazione Tkinter - place()", font=("TkDefaultFont", 18, "bold"), relief="sunken", bd=3)
		lbl_titolo.grid(row=0, column=0, padx=20, columnspan=3, sticky="ew", ipady=10)
		
		#Introduzione
		lbl_intro1=tk.Label(mf, text="Il metodo place() consente di posizionare un widget Tkinter in una posizione specifica all'interno del frame o della finestra.\nÈ possibile posizionare il widget in modo assoluto o relativo rispetto al frame o alla finestra genitore.", font=("TkDefaultFont", 10, ""))
		lbl_intro1.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky="ew")
		
		#Sintassi
		lbl_intro2=tk.Label(mf, text="Sintassi: widget.place(attributi)", font=("TkDefaultFont", 10, ""))
		lbl_intro2.grid(row=2, column=0, padx=20, columnspan=3, sticky="ew")
		
		#Attributi
		lbl_attr=tk.Label(mf, text="Ecco l'elenco degli attributi:", font=("TkDefaultFont", 10, ""))
		lbl_attr.grid(row=3, column=0, padx=20, pady=10, columnspan=3, sticky="ew")
		
##################################################################################################################################################
		
		#Finestra attributo 'x'
		def open_win_x():
			win_x = tk.Toplevel()
			win_x.title("Attributo 'x'")
			win_x.geometry("600x60")
			tk.Label(win_x, text='Questa label è spostata di 50px orizzontalmente', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(x=50)
			tk.Label(win_x, text='Codice: tk.Label(win_x, text="Questa label è spostata di 50px orizzontalmente").place(x=50)').place(y=30)
		
		#Finestra attributo 'y'
		def open_win_y():
			win_y = tk.Toplevel()
			win_y.title("Attributo 'y'")
			win_y.geometry("600x110")
			tk.Label(win_y, text='Questa label è spostata di 50px verticalmente', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(y=50)
			tk.Label(win_y, text='Codice: tk.Label(win_y, text="Questa label è spostata di 50px verticalmente").place(y=50)').place(y=80)
		
		#Finestra attributo 'relx'
		def open_win_relx():
			win_relx = tk.Toplevel()
			win_relx.title("Attributo 'relx'")
			win_relx.geometry("1000x60")
			tk.Label(win_relx, text='Questa label è posizionata orizzontalmente al centro del frame', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(relx=0.5)
			tk.Label(win_relx, text='Codice: tk.Label(win_relx, text="Questa label è posizionata orizzontalmente al centro del frame").place(relx=0.5)').place(y=30)
		
		#Finestra attributo 'rely'
		def open_win_rely():
			win_rely = tk.Toplevel()
			win_rely.title("Attributo 'rely'")
			win_rely.geometry("670x110")
			tk.Label(win_rely, text='Questa label è posizionata verticalmente al centro del frame', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(rely=0.5)
			tk.Label(win_rely, text='Codice: tk.Label(win_rely, text="Questa label è posizionata verticalmente al centro del frame").place(rely=0.5)').place(y=80)
		
		#Finestra attributo 'relwidth'
		def open_win_relwidth():
			win_relwidth = tk.Toplevel()
			win_relwidth.title("Attributo 'relwidth'")
			win_relwidth.geometry("600x60")
			tk.Label(win_relwidth, text='Questa label è larga quanto il frame', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(relwidth=1)
			tk.Label(win_relwidth, text='Codice: tk.Label(win_relwidth, text="Questa label è larga quanto il frame").place(relwidth=1)').place(y=30)
		
		#Finestra attributo 'relheight'
		def open_win_relheight():
			win_relheight = tk.Toplevel()
			win_relheight.title("Attributo 'relheight'")
			win_relheight.geometry("850x60")
			tk.Label(win_relheight, text='Questa label è alta quanto il frame', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(relheight=1)
			tk.Label(win_relheight, text='Codice: tk.Label(win_relheight, text="Questa label è alta quanto il frame").place(relheight=1)').place(x=300)
		
		#Finestra attributo 'width'
		def open_win_width():
			win_width = tk.Toplevel()
			win_width.title("Attributo 'width'")
			win_width.geometry("600x60")
			tk.Label(win_width, text='Questa label è larga 500px', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(width=500)
			tk.Label(win_width, text='Codice: tk.Label(win_width, text="Questa label è larga 500px").place(width=500)').place(y=30)
		
		#Finestra attributo 'height'
		def open_win_height():
			win_height = tk.Toplevel()
			win_height.title("Attributo 'height'")
			win_height.geometry("600x150")
			tk.Label(win_height, text='Questa label è alta 100px', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(height=100)
			tk.Label(win_height, text='Codice: tk.Label(win_height, text="Questa label è alta 100px").place(height=100)').place(y=120)
		
		#Finestra attributo 'anchor'
		def open_win_anchor():
			win_anchor = tk.Toplevel()
			win_anchor.title("Attributo 'anchor'")
			win_anchor.geometry("730x150")
			tk.Label(win_anchor, text='Questa label è ancorata al centro del frame', font=("TkDefaultFont", 10, "bold"), bg="yellow").place(relx=0.5, rely=0.5, anchor="center")
			tk.Label(win_anchor, text='Codice: tk.Label(win_anchor, text="Questa label è ancorata al centro del frame").place(relx=0.5, rely=0.5, anchor="center")').place(y=120)
		
		#Finestra attributo 'bordermode'
		def open_win_bordermode():
			win_bordermode = tk.Toplevel()
			win_bordermode.title("Attributo 'bordermode'")
			win_bordermode.geometry("500x100")
			
			f1 = tk.Frame(win_bordermode, borderwidth=5, relief="sunken", width=370, height=50, bg="yellow")
			f1.pack()
			l1 = tk.Label(f1, text='l1.place(x=10, y=10, bordermode="outside")', font=("TkDefaultFont", 10, "bold"), bg="yellow")
			l1.place(x=10, y=10, bordermode="outside")

			f2 = tk.Frame(win_bordermode, borderwidth=5, relief="sunken", width=370, height=50, bg="yellow")
			f2.pack()
			l2 = tk.Label(f2, text='l2.place(x=10, y=10, bordermode="inside")', font=("TkDefaultFont", 10, "bold"), bg="yellow")
			l2.place(x=10, y=10, bordermode="inside")
		
##################################################################################################################################################
		
		#Attributo 'x'
		btn_x=tk.Button(mf, text="x", command=open_win_x, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_x.grid(row=4, column=0, padx=20, pady=(10,0), sticky="ew")
		lbl_x=tk.Label(mf, text="Specifica la posizione orizzontale in pixel del widget rispetto al lato sinistro del frame o della finestra genitore.\nIl valore predefinito è 0.", relief="sunken", bd=3)
		lbl_x.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")
		
		#Attributo 'y'
		btn_y=tk.Button(mf, text="y", command=open_win_y, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_y.grid(row=4, column=1, padx=20, pady=(10, 0), sticky="ew")
		lbl_y=tk.Label(mf, text="Specifica la posizione verticale in pixel del widget rispetto al lato superiore del frame o della finestra genitore.\nIl valore predefinito è 0.", relief="sunken", bd=3)
		lbl_y.grid(row=5, column=1, padx=20, pady=(0, 20), sticky="ew")
		
		#Attributo 'relx'
		btn_relx=tk.Button(mf, text="relx", command=open_win_relx, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_relx.grid(row=6, column=0, padx=20, sticky="ew")
		lbl_relx=tk.Label(mf, text="Specifica la posizione orizzontale del widget in modo relativo alla larghezza del frame o della finestra genitore.\nIl valore predefinito è 0.0, che corrisponde al lato sinistro del frame o della finestra genitore.\nIl valore di relx è compreso tra 0.0 e 1.0.", relief="sunken", bd=3)
		lbl_relx.grid(row=7, column=0, padx=20, sticky="ew")
		
		#Attributo 'rely'
		btn_rely=tk.Button(mf, text="rely", command=open_win_rely, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_rely.grid(row=6, column=1, padx=20, sticky="ew")
		lbl_rely=tk.Label(mf, text="Specifica la posizione verticale del widget in modo relativo all'altezza del frame o della finestra genitore.\nIl valore predefinito è 0.0, che corrisponde al lato superiore del frame o della finestra genitore.\nIl valore di rely è compreso tra 0.0 e 1.0.", relief="sunken", bd=3)
		lbl_rely.grid(row=7, column=1, padx=20, sticky="ew")
		
		#Attributo 'relwidth'
		btn_relwidth=tk.Button(mf, text="relwidth", command=open_win_relwidth, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_relwidth.grid(row=8, column=0, padx=20, pady=(20, 0), sticky="ew")
		lbl_relwidth=tk.Label(mf, text="Specifica la larghezza del widget in modo relativo alla larghezza del frame o della finestra genitore.\nIl valore predefinito è 0.0, che significa che la larghezza del widget sarà determinata dal contenuto.\nIl valore di relwidth è compreso tra 0.0 e 1.0.", relief="sunken", bd=3)
		lbl_relwidth.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="ew")
		
		#Attributo 'relheight'
		btn_relheight=tk.Button(mf, text="relheight", command=open_win_relheight, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_relheight.grid(row=8, column=1, padx=20, pady=(20, 0), sticky="ew")
		lbl_relheight=tk.Label(mf, text="Specifica l'altezza del widget in modo relativo all'altezza del frame o della finestra genitore.\nIl valore predefinito è 0.0, che significa che l'altezza del widget sarà determinata dal contenuto.\nIl valore di relheight è compreso tra 0.0 e 1.0.", relief="sunken", bd=3)
		lbl_relheight.grid(row=9, column=1, padx=20, pady=(0, 20), sticky="ew")
		
		#Attributo 'width'
		btn_width=tk.Button(mf, text="width", command=open_win_width, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_width.grid(row=10, column=0, padx=20, sticky="ew")
		lbl_width=tk.Label(mf, text="Specifica la larghezza del widget in pixel. Il valore predefinito è determinato dal contenuto del widget.", relief="sunken", bd=3)
		lbl_width.grid(row=11, column=0, padx=20, sticky="ew")
		
		#Attributo 'height'
		btn_height=tk.Button(mf, text="height", command=open_win_height, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_height.grid(row=10, column=1, padx=20, sticky="ew")
		lbl_height=tk.Label(mf, text="Specifica l'altezza del widget in pixel. Il valore predefinito è determinato dal contenuto del widget.", relief="sunken", bd=3)
		lbl_height.grid(row=11, column=1, padx=20, sticky="ew")
		
		#Attributo 'anchor'
		btn_anchor=tk.Button(mf, text="anchor", command=open_win_anchor, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_anchor.grid(row=12, column=0, padx=20, pady=(20, 0), sticky="ew")
		lbl_anchor=tk.Label(mf, text="Specifica l'ancoraggio del widget rispetto alla sua posizione. Il valore predefinito è 'nw' (nord-ovest).\nAltri valori possibili sono 'n', 'ne', 'e', 'se', 's', 'sw', 'w' e 'center'.", relief="sunken", bd=3)
		lbl_anchor.grid(row=13, column=0, padx=20, pady=(0, 20), sticky="ew")
		
		#Attributo 'bordermode'
		btn_bordermode=tk.Button(mf, text="bordermode", command=open_win_bordermode, relief="sunken", bd=3, font=("TkDefaultFont", 10, "bold"))
		btn_bordermode.grid(row=12, column=1, padx=20, pady=(20, 0), sticky="ew")
		lbl_bordermode=tk.Label(mf, text="Specifica il modo di calcolare la posizione del widget in relazione al bordo della finestra o del frame genitore.\n'outside' conta x e y dall'angolo in alto a sinistra del frame compreso il bordo, 'inside' le conta senza il bordo.", relief="sunken", bd=3)
		lbl_bordermode.grid(row=13, column=1, padx=20, pady=(0, 20), sticky="ew")

def main():
	f=Finestra("Galeasso - Relazione Tkinter - place()")
	messagebox.showinfo("Benvenuto!", "In questa guida viene spiegato il metodo place() con tutti i suoi attributi. Clicca su quello che ti interessa per vedere l'esempio e il codice.")
	f.mainloop()
main()
