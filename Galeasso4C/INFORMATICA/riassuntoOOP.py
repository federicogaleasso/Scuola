import copy

class punto():

	def __init__(self,valx=0,valy=0):
		self.set_x(valx)
		self.set_y(valy)

	def __str__(self):
		return "("+str(self.get_x())+","+str(self.get_y())+")"

	def set_x(self,vx):
		self.__x=vx

	def get_x(self):
		return self.__x
	
	def set_y(self,vy):
		self.__y=vy

	def get_y(self):
		return self.__y


class rettangolo():

	def __init__(self,valtezza,vlarghezza,objpt):
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

	def set_verticeAS(self,opt):
		self.__verticeAS=opt

	def get_verticeAS(self):
		return self.__verticeAS

	def __str__(self):
		return "Altezza: "+str(self.get_altezza())+"\nLarghezza: "+str(self.get_larghezza())+"\nVertice AS: "+str(self.get_verticeAS())
#("+str(self.get_verticeAS().get_x())+","+str(self.get_verticeAS().get_y())+")

print("Creo un nuovo obj punto:")
nuovopt=punto(3,4)
print(nuovopt)

print("Creo un nuovo rettangolo con l'obj punto di sopra come verticeAS...")
nuovoret=rettangolo(200,100,nuovopt)
print("nuovoret:\n",nuovoret)

#print(nuovoret)

print("Creo ret2 come alias di nuovoret...")
ret2=nuovoret
print("Ret2:\n",ret2)

print("Re-imposto a 7 la coordinata x dell'obj punto di sopra...")
nuovopt.set_x(7)
print("Ret2 dopo la modifica della x del punto:\n",ret2)

print("Creo ret3 come copia clone indipendente di nuovoret...")
ret3 = copy.copy(nuovoret)
print("Ret3:\n",ret3)

print("Re-imposto a 333 l'altezza di nuovoret...")
nuovoret.set_altezza(333)
print("Re-imposto a 13 la coordinata y dell'obj punto di sopra...")
nuovopt.set_y(13)

print("Stampo Ret3 che risente solo in parte delle modifiche appena fatte:\n",ret3)
print("Stampo nuovoret:\n",nuovoret)
