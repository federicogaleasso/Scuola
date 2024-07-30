#GALEASSO FEDERICO 4C 23/9/2022 COMPITO INPUT NOMEUTENTE

#Scrivere un programma che richieda cognome, nome, classe, specializzazione e data di nascita all'utente.
#Creare il nome utente composto da:
#- prime tre lettere del cognome
#- prime tre lettere del nome
#- ultime due cifre della data di nascita
#- le due lettere della classe (es. 4C)
#- prime tre lettere della specializzazione
#L'output del nome utente dovrà essere il seguente:
#CogNomAnno_classe-spec

nome=input("Inserisci il tuo nome: ")
cognome=input("Inserisci il tuo cognome: ")
classe=input("Inserisci la tua classe: ")
spec=input("Inserisci la tua specializzazione: ")
datanascita=input("Inserisci la tua data di nascita: ")
print("\n"+"*"*27)
resoconto=print("Ecco i dati appena inseriti")
print("*"*27)
print("Nome:",nome)
print("Cognome:",cognome)
print("Classe:",classe)
print("Specializzazione:",spec)
print("Data di nascita:",datanascita)
print("*"*27)
nomeutente=cognome[0:3]+nome[0:3]+datanascita[-2:]+"_"+classe+"-"+spec[0:3]
print("\nIl nome utente è il seguente:"+"\033[1m"+"\033[92m",nomeutente)
