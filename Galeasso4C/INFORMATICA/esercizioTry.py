#GALEASSO FEDERICO 4C 14/10/2022 ESERCIZIO TRY/EXCEPT/FINALLY

flag=False
while flag==False:
	str_num=input("Inserisci un numero intero: ")
	try:
		numimmesso=int(str_num)
		flag=True
	except:
		print("Non hai messo un numero")
print("Uscita del programma in corso...")
