def carica():
	Banco={}
	lista=list(sorted(set("BEKIMSULEJMANI")))
	lung=len(lista)
	for i in range(lung):
		prod=input(f"Inserire il prodotto per {lista[i]:}: ")
		quant=int(input("Inserire la quantita: "))
		Banco[lista[i]]=[prod, quant]
	#print(Banco)
	estrazione(Banco)

def estrazione(Banco):
	print()
	flag=False
	while flag==False:
		lett=input("Inserire una lettera dell'alfabeto: ")
		if lett in Banco:
			Banco[lett][1]-=1
			print()
			print(f"Hai vinto un/una {Banco[lett][0]:}")
			#if Banco[lett][1]==0:
				#Banco=Banco.popitem() --> non funziona
			#print(Banco)
			flag=True
		else:
			print("La lettera inserita non esiste.")
			flag=False
	stampa(Banco)
		
def stampa(Banco):
	print()
	print(f"{'Biglietto':>10}{'Premio':>10}  {'Quantita':>10}")
	for chiave in Banco:
		print(f" {chiave:<10}   {Banco[chiave][0]:<10}{Banco[chiave][1]:<10}")

carica()
