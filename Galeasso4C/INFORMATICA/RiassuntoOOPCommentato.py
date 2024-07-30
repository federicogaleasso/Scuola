#GALEASSO FEDERICO 4C 12/12/2022 APPUNTI CPOMMENTATI OOP

# !IMPORTANTE! --> ogni classe è MUTABILE

import copy	#crea una copia INDIPENDENTE (doppio spazio occupato in memoria). la deecopy crea una copia di tutte le classi, e non una copia di primo livello come la copy

class punto():	#creazione classe punto

	def __init__(self,valx=0,valy=0):	# __init__ --> costruttore, inizializza gli attributi. Il passaggio tra setter e getter permette di fare dei controlli di errore (incapsulamento --> meccanismo di protezione degli attributi per evitare che vengano fatto malamente delle modifiche)
		self.set_x(valx)
		self.set_y(valy)

	def __str__(self):	#__str__ --> metodo ritorna una stringa fissa (un'insieme di stringhe concatenate, serve soprattutto per debug)
		return "("+str(self.get_x())+","+str(self.get_y())+")"

	def set_x(self,vx):	# set --> setter (inizializza), metodo pubblico
		self.__x=vx	# .__ --> attributo privato, ci si accede solo all'interno 

	def get_x(self):	# get --> getter (estrapola), metodo pubblico
		return self.__x	# .__ --> attributo privato, ci si accede solo all'interno
	
	def set_y(self,vy):
		self.__y=vy

	def get_y(self):
		return self.__y


class rettangolo():

	def __init__(self,valtezza,vlarghezza,objpt):	#In questo caso, alla creazione di una nuova istanza rettangolo dobbiamo per forza inserire un valore (perchè non c'è --> =0)
		self.set_altezza(valtezza)
		self.set_larghezza(vlarghezza)
		self.set_verticeAS(objpt)

	def set_altezza(self,valtez):
		self.__altezza=valtez

	def get_altezza(self):
		return self.__altezza

	def set_larghezza(self,vlarghez):
		self.__larghezza=vlarghez

	def get_larghezza(self):
		return self.__larghezza

	def set_verticeAS(self,opt):	#oggetto mutabile di tipo punto che gli abbiamo passato quando abbiamo creato la istanza rettangolo
		self.__verticeAS=opt

	def get_verticeAS(self):
		return self.__verticeAS

	def __str__(self):
		return "Altezza: "+str(self.get_altezza())+"\nLarghezza: "+str(self.get_larghezza())+"\nVertice AS: "+str(self.get_verticeAS()) #..."+str(self.get_verticeAS(). Con il + --> l'oggetto da problemi se viene concatenato con una stringa (si deve fare il casting in str). Con la , --> non da problemi e non serve il casting in str

#("+str(self.get_verticeAS().get_x())+","+str(self.get_verticeAS().get_y())+")

print("Creo un nuovo obj punto:")
nuovopt=punto(3,4)	#istanziazione --> creazione di una nuova istanza della classe punto. Ogni istanza è DIPENDENTE dalla sua classe: ogni modifica avverrà nella classe e nelle sue istanze
print(nuovopt)

print("Creo un nuovo rettangolo con l'obj punto di sopra come verticeAS...")
nuovoret=rettangolo(200,100,nuovopt)	#istanziazione --> creazione di una nuova istanza della classe rettangolo. Ogni istanza è DIPENDENTE dalla sua classe: ogni modifica avverrà nella classe e nelle sue istanze. nuovopt --> viene passato come object reference, in memoria c'è UNA volta sola
print("nuovoret:\n",nuovoret)

#print(nuovoret)

print("Creo ret2 come alias di nuovoret...")
ret2=nuovoret	#creazione di un alias (nome alternativo) --> ogni modifica avviene in entrambe le parti (STESSA cella di memoria)
print("Ret2:\n",ret2)

print("Re-imposto a 7 la coordinata x dell'obj punto di sopra...")
nuovopt.set_x(7)	#metodo della classe punto --> viene cambiato il valore della x a 7. Sia che stampiamo ret2 o nuovoret la x diventa 7
print("Ret2 dopo la modifica della x del punto:\n",ret2)

print("Creo ret3 come copia clone indipendente di nuovoret...")
ret3 = copy.copy(nuovoret)	#copy è un metodo che serve a creare una copia INDIPENDENTE: ogni modifica avverrà SOLO nella classe e NON nelle sue istanze. Altezza: IMMUTABILE, Larghezza: MUTABILE, Vertice AS: MUTABILE (è la classe punto!!!)
print("Ret3:\n",ret3)

print("Re-imposto a 333 l'altezza di nuovoret...")
nuovoret.set_altezza(333)	#Altezza cambia solo in nuovoret e non in ret3 (ret3 è una copia INDIPENDENTE)
print("Re-imposto a 13 la coordinata y dell'obj punto di sopra...")
nuovopt.set_y(13)	#La y di Vertice AS cambia in nuovoret e in ret3, perchè Vertice AS è la classe punto (Le classi sono MUTABILI)

print("Stampo Ret3 che risente solo in parte delle modifiche appena fatte:\n",ret3)
print("Stampo nuovoret:\n",nuovoret)
