import os

os.system("cls")

class esibizione():
	def __init__(self, titolo = "", durata = 0):
		self.settitolo(titolo)
		self.setdurata(durata)

	def settitolo(self, titolo):
		self.__tit = titolo

	def gettitolo(self):
		return self.__tit
	
	def setdurata(self, durata):
		self.__dur = durata
	
	def getdurata(self):
		return self.__dur

class canto(esibizione):
	def __init__(self, genMusic = "", titolo = "", durata = 0):
		super().__init__(titolo, durata)
		self.setGenMusic(genMusic)

	def setGenMusic(self, genMusic):
		self.__gnMusic = genMusic

	def getGenMusic(self):
		return self.__gnMusic
	
	def __repr__(self):
		return f"Titolo: {self.gettitolo()}\nGenere: {self.getGenMusic()}\nDurata: {self.getdurata()}minuti\n\n"

class ginnastica(esibizione):
	def __init__(self, attrezzo = "", titolo = "", durata = 0):
		super().__init__(titolo, durata)
		self.setAttrezzo(attrezzo)

	def setAttrezzo(self, attrezzo):
		self.__atr = attrezzo

	def getAttrezzo(self):
		return self.__atr
	
	def __repr__(self):
		return f"Titolo: {self.gettitolo()}\nAttrezzo: {self.getAttrezzo()}\nDurata: {self.getdurata()}minuti\n\n"

class poesia(esibizione):
	def __init__(self, titolo = "", durata = 0):
		super().__init__(titolo, durata)
	
	def __repr__(self):
		return f"Titolo: {self.gettitolo()}\nDurata: {self.getdurata()}minuti\n\n"

class partecipante():
	def __init__(self, nome = "", cognome = "", sesso = "", eta = 0, tipologia = ""):
		self.setnome(nome)
		self.setcognome(cognome)
		self.setsesso(sesso)
		self.seteta(eta)
		self.settipologia(tipologia)
	
	def setnome(self, nome):
		self.__nm = nome
	
	def getnome(self):
		return self.__nm
	
	def setcognome(self, cognome):
		self.__cog = cognome
	
	def getcognome(self):
		return self.__cog
	
	def setsesso(self, sesso):
		self.__ses = sesso
	
	def getsesso(self):
		return self.__ses
	
	def seteta(self, eta):
		self.__et = eta
	
	def geteta(self):
		return self.__et
	
	def settipologia(self, tipologia):
		self.__tip = tipologia
	
	def gettipologia(self):
		return self.__tip
	
	def __repr__(self):
		return f"Nome: {self.getnome()}\nCognome: {self.getcognome()}\nSesso: {self.getsesso()}\nEta: {self.geteta()}\nTipologia: {self.gettipologia()}\n\n"


class manifestazione():
	def __init__(self, nome = ""):
		self.setnome(nome)
		self.__aggpart = []
		self.__aggcant = dict()
		self.__aggpoeti = dict()
		self.__aggGinn = dict()
		
	def setnome(self, nome):
		self.__nm = nome
	
	def getnome(self):
		return self.__nm
	
	def aggiungipartecipante(self, p1):
		self.__aggpart.append(p1)
	
	def getpartecipanti(self):
		return self.__aggpart
	
	def aggiungicantante(self, p1, e1):
		self.__aggcant[p1] = e1 
	
	def getcantante(self):
		return self.__aggcant
	
	def aggiungipoeta(self, p1, e1):
		self.__aggpoeti[p1] = e1
	
	def getpoeta(self):
		return self.__aggpoeti
	
	def aggiungiginnasta(self, p1, e1):
		self.__aggGinn[p1] = e1

	def getginnasta(self):
		return self.__aggGinn
	
	def trova(self, nom, cog):
		for parte in self.getpartecipanti():
			if parte.getnome() == nom and parte.getcognome() == cog:
				if parte.gettipologia() == "partecipante":
					return "Semplice partecipante"
				else:
					return parte.gettipologia()
		return "Non esiste un partecipante con questo nome"
	
	def elimina(self, nom, cog):
		for parte in self.getpartecipanti():
			if parte.getnome() == nom and parte.getcognome() == cog:
				return "Partecipante eliminato"
		return "Partecipante non trovato"


def main():
	#vari esebitori
	cantoP2 = canto("dramma", "il dubbio", 4)
	cantoP3 = canto("commedia", "il grande giorno", 5)
	poetaP4 = poesia("chi va la?", 2)
	ginnastaP5 = ginnastica("anello", "il circolo del cerchio", 7)
	poetaP6 = poesia("dopo di te!", 4)

	#aggingo e setto partecipanti
	p1 = partecipante("marco", "rossi", "M", 23, "partecipante")
	p2 = partecipante("giovanni", "bianchi", "M", 20, "canto")
	p3 = partecipante("paola", "dessi", "F", 28, "canto")
	p4 = partecipante("roberta", "case", "F", 43, "poeta")
	p5 = partecipante("franco", "gio", "M", 33, "ginnasta")
	p6 = partecipante("luca", "alba", "M", 21, "poeta")

	mani = manifestazione("corrida")
	mani.aggiungipartecipante(p1)
	mani.aggiungipartecipante(p2)
	mani.aggiungipartecipante(p3)
	mani.aggiungipartecipante(p4)
	mani.aggiungipartecipante(p5)
	mani.aggiungipartecipante(p6)

	#cosa esibiscono
	mani.aggiungicantante(p2, cantoP2)
	mani.aggiungicantante(p3, cantoP3)
	mani.aggiungipoeta(p4, poetaP4)
	mani.aggiungiginnasta(p5, ginnastaP5)
	mani.aggiungipoeta(p6, poetaP6)

	print("-" * 10, " Trova Partecipante ", 10 * "-")
	nomeTry = input("Inserisci il nome del partecipante da trovare: ")
	cogTry = input("Inserisci il cognome del partecipante da trovare: ")
	resT = mani.trova(nomeTry, cogTry)
	
	if resT == "canto":
		dizcant = mani.getcantante()
		for chiave in dizcant:
			if chiave.getnome() == nomeTry and chiave.getnome() == nomeTry:
				tit = dizcant[chiave].gettitolo()
				dur = dizcant[chiave].getdurata()
		print(f"La sua performance si intitola {tit} e dura {dur}")

	elif resT == "poeta":
		dizcant = mani.getpoeta()
		for chiave in dizcant:
			if chiave.getnome() == nomeTry and chiave.getnome() == nomeTry:
				tit = dizcant[chiave].gettitolo()
				dur = dizcant[chiave].getdurata()
		print(f"La sua performance si intitola {tit} e dura {dur}")

	elif resT == "ginnasta":
		dizcant = mani.getginnasta()
		for chiave in dizcant:
			if chiave.getnome() == nomeTry and chiave.getnome() == nomeTry:
				tit = dizcant[chiave].gettitolo()
				dur = dizcant[chiave].getdurata()
		print(f"La sua performance si intitola {tit} e dura {dur}minuti")

	else:
		print(resT)

	print("\n", "-" * 10, " Elimina Partecipante ", 10 * "-")
	ElnomeTry = input("Inserisci il nome del partecipante da eliminare: ")
	ElcogTry = input("Inserisci il cognome del partecipante da eliminare: ")
	resEl = mani.elimina(ElnomeTry, ElcogTry)
	print(resEl, "\n")

	print(mani.getpartecipanti())
	print("-" * 50)
	print(mani.getcantante())
	print(mani.getpoeta())
	print(mani.getginnasta())

main()
