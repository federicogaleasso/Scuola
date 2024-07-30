#GALEASSO FEDERICO 4C 10/2/2023 ESERCIZIO IN CLASSE - CALCIO OOP

#Creare una classe Squadra che rappresenti una squadra di calcio e abbia come attributi il nome della squadra, il numero di partite vinte, il numero di partite perse e il numero di partite pareggiate. La classe deve disporre di opportuni metodi per impostare o visualizzare gli attributi, un metodo punti() che restituisce quanti punti ha in campionato (ogni partita vinta vale 3 punti, ogni partita pareggiata 1, quelle perse 0) e un metodo inizioanno() che azzera il numero di partite vinte, pareggiate e perse.
#Nello specifico, utilizzando l'overloading degli operatori il programma deve permettere di aggiornare i punti in campionato di una istanza di squadra nel seguente modo:
#a. Milan + 4 --> somma 4 punti dovuto a 4 partite pareggiate
#b. Milan * 2 --> somma 6 punti relativi alle 2 partite vinte
#c. Milan - Juventus --> restituisce la differenza dei punteggi delle due squadre. L'output di questa operazione deve essere sempre del tipo "Il Milan ha 7 punti in più della Juventus", oppure "La Juventus ha 3 punti in più del Milan"
#d. int(Milan) --> deve restituire il numero di punti in campionato
#La stampa di un'istanza deve visualizzare il nome della squadra, il numero di partite vinte, il numero di partite pareggiate, il numero di partite perse

import os
def clearScreen():
	os.system("clear")
clearScreen()

# classe Squadra()
class Squadra():
	def __init__(self, nome='', vinte=0, perse=0, pareggiate=0):
		self.set_nome(nome)
		self.set_vinte(vinte)
		self.set_perse(perse)
		self.set_pareggiate(pareggiate)
		  
	def set_nome(self, nome):
		self.__nome = nome
		
	def get_nome(self):
		return self.__nome
		
	def set_vinte(self, vinte):
		self.__vinte = vinte
		
	def get_vinte(self):
		return self.__vinte
		
	def set_perse(self, perse):
		self.__perse = perse
		
	def get_perse(self):
		return self.__perse
		
	def set_pareggiate(self, pareggiate):
		self.__pareggiate = pareggiate
		
	def get_pareggiate(self):
		return self.__pareggiate
		
	def punti(self):
		return self.get_vinte()*3+self.get_pareggiate()
	
	def inizioanno(self):
		self.get_vinte=0
		self.get_perse=0
		self.get_pareggiate=0
		
	def __str__(self):
		return f'{self.get_nome()}:\nVinte: {self.get_vinte()} | Perse: {self.get_perse()} | Pareggiate: {self.get_pareggiate()}'
	
	def __add__(self, n):
		return self.punti()+n
		
	def __mul__(self, n):
		return self.punti()+(n*3)
		
	def __sub__(self, squadra2):
		differenza_punti=self.punti()-squadra2.punti()
		
		if differenza_punti > 0:
			return f"Il Milan ha {differenza_punti} punti in più della Juventus"
		else:
			#Il ' - ' davanti a alla variabile ' differenza_punti ' serve ad invertire il suo segno.
			#Nell'else il suo segno quindi diventerà ' + ' (- * - = +)
			return f"La Juventus ha {-differenza_punti} punti in più del Milan"
	
	def __int__(self):
		return self.punti()
		
# main()
def main():
	milan=Squadra("Milan", 3, 1, 2)
	juventus=Squadra("Juventus", 2, 4, 1)
	
	print(milan)
	print("Punteggio:",milan.punti(),"\n")
	
	print(juventus)
	print("Punteggio:",juventus.punti(),"\n")
	
	print("Overloading operatore __add__")
	print("Punteggio Milan:",milan+4,"\n")
	
	print("Overloading operatore __mul__")
	print("Punteggio Milan:",milan*2,"\n")
	
	print("Overloading operatore __sub__")
	print(milan-juventus,"\n")
	
	print("Overloading operatore __int__")
	print("Punteggio Milan:",int(milan))
main()
