#GALEASSO FEDERICO 4C 26/04/2023 COMPITO - RUBRICA XML

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def clearScreen():
	os.system("clear")
clearScreen()

#funzione indenta()
def indenta(nomef_in="rubricaXML.xml", nomef_out="rubricaXML.xml"):
	dom = minidom.parse(nomef_in)
	with open(nomef_out, 'w', encoding='UTF-8') as fh:
		 dom.writexml(fh, indent='', addindent='	', newl='\n', encoding='UTF-8')		 

rubrica = ET.Element("rubrica")

#Utente 1
utente = ET.SubElement(rubrica, "utente")
utente.set("sesso", "M")
utente.set("titolo", "prof.")
utente.set("soprannome", "...")
nome = ET.SubElement(utente, "nome")
nome.text = "Mario"
cognome = ET.SubElement(utente, "cognome")
cognome.text = "Rossi"
indirizzo = ET.SubElement(utente, "indirizzo")
via = ET.SubElement(indirizzo, "via")
via.set("numero", "40")
via.text = "Pellengo"
cap = ET.SubElement(indirizzo, "cap")
cap.text = "12033"
telefono = ET.SubElement(utente, "telefono")
telefono.set("tipo", "cellulare")
telefono.text = "3338926713"

#Utente 2
utente = ET.SubElement(rubrica, "utente")
utente.set("sesso", "F")
utente.set("titolo", "amica")
utente.set("soprannome", "...")
nome = ET.SubElement(utente, "nome")
nome.text = "Giulia"
cognome = ET.SubElement(utente, "cognome")
cognome.text = "Verdi"
indirizzo = ET.SubElement(utente, "indirizzo")
via = ET.SubElement(indirizzo, "via")
via.set("numero", "10")
via.text = "Monte Bianco"
cap = ET.SubElement(indirizzo, "cap")
cap.text = "12030"
telefono = ET.SubElement(utente, "telefono")
telefono.set("tipo", "cellulare")
telefono.text = "3399137810"

tree = ET.ElementTree(rubrica)
tree.write("rubricaXML.xml")
indenta("rubricaXML.xml", "rubricaXML.xml")

#Ricerca del telefono
nTelefono_find = input("Inserisci un numero di telefono da ricercare: ")
for utente in rubrica.findall("utente"):
	rank = utente.find("telefono").text
	if nTelefono_find == rank:
		nome = utente.find("nome").text
		cognome = utente.find("cognome").text
		print(f"Telefono trovato!\nLa persona cercata si chiama {nome} {cognome}")

#Ricerca del cognome		
cognome_find = input("\nInserisci un cognome da ricercare: ")
for utente in rubrica.findall("utente"):
	rank = utente.find("cognome").text
	if cognome_find == rank:
		nome = utente.find("nome").text
		cognome = utente.find("cognome").text
		print(f"Cognome trovato!\nLa persona cercata si chiama {nome} {cognome}")

#Stampa degli uomini
print("\nEcco gli utenti uomini: ")		
for utente in rubrica.findall("utente"):
	rank = utente.get("sesso")
	if "M" == rank:
		nome = utente.find("nome").text
		cognome = utente.find("cognome").text
		print(nome, cognome)

#Eliminazione utente
nome_delete = input("\nInserisci il nome dell'utente eliminare: ")
cognome_delete = input("Inserisci il cognome dell'utente eliminare: ")
for utente in rubrica.findall("utente"):
	rank1 = utente.find("nome").text
	rank2 = utente.find("cognome").text
	if nome_delete == rank1 and cognome_delete == rank2:
		rubrica.remove(utente)
		tree = ET.ElementTree(rubrica)
		tree.write("rubricaXML.xml")
		indenta("rubricaXML.xml", "rubricaXML.xml")
		print("Utente eliminato!")
