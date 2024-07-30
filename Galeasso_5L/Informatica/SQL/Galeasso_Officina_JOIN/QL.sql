-- Galeasso Federico 5L 14/04/2024 - Officina QL

USE Officina;

/* QUERY A IMPLICITA: Elenco delle auto di Consiglio */
\! echo "*** QUERY A - IMPLICITA ***"
SELECT Auto.targa, Cliente.cognome
FROM Auto, Cliente
WHERE Cliente.id_cliente = Auto.cliente
AND Cliente.cognome = "Consiglio";

/* QUERY A ESPLICITA: Elenco delle auto di Consiglio */
\! echo "*** QUERY A - ESPLICITA ***"
SELECT A.targa, C.cognome
FROM Auto AS a 
JOIN Cliente AS c
ON c.id_cliente = A.cliente
WHERE C.cognome = "Consiglio";

/* QUERY B: Elenco dei clienti che abitano a Saluzzo */
\! echo "*** QUERY B ***"
SELECT Cliente.nome, Cliente.cognome, Cliente.citta
FROM Cliente
WHERE Cliente.citta = "Saluzzo";

/* Query 1 IMPLICITA: Tutti gli interventi fatti sui modelli Renault */
\! echo "*** QUERY 1 - IMPLICITA ***"
SELECT Intervento.tipo_intervento, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Intervento, Auto, Modello, Costruttore
WHERE Intervento.targa = Auto.targa
AND Auto.modello = Modello.id_modello
AND Modello.costruttore = Costruttore.id_costruttore
AND Costruttore.casa_automobilistica = "Renault";

/* Query 1 ESPLICITA: Tutti gli interventi fatti sui modelli Renault */
\! echo "*** QUERY 1 - ESPLICITA ***"
SELECT Intervento.tipo_intervento, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Intervento 
JOIN Auto ON Intervento.targa = Auto.targa
JOIN Modello ON Modello.id_modello = Auto.modello 
JOIN Costruttore ON Costruttore.id_costruttore = Modello.costruttore
WHERE Costruttore.casa_automobilistica = "Renault";

/* Query 3: Elenco degli interventi contenenti nella descrizione “cambio” - valida anche l'opzione LIKE */
\! echo "*** QUERY 3 ***"
SELECT Intervento.id_intervento, Intervento.tipo_intervento
FROM Intervento
WHERE Intervento.tipo_intervento = "cambio";

/* Query 4 IMPLICITA: Elenco dei clienti aventi auto d'epoca */
\! echo "*** QUERY 4 - IMPLICITA ***"
SELECT Cliente.nome, Cliente.cognome, Auto.epoca
FROM Cliente, Auto
WHERE Cliente.id_cliente = Auto.cliente
AND Auto.epoca = "epoca";

/* Query 4 ESPLICITA: Elenco dei clienti aventi auto d'epoca */
\! echo "*** QUERY 4 - ESPLICITA ***"
SELECT Cliente.nome, Cliente.cognome, Auto.epoca
FROM Cliente
JOIN AUTO ON Cliente.id_cliente = Auto.cliente
WHERE Auto.epoca = "epoca";

/* Query 6 IMPLICITA: Elenco di tutti i modelli Ford, ordinate per anno */
\! echo "*** QUERY 6 - IMPLICITA ***"
SELECT Auto.anno, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Auto, Modello, Costruttore
WHERE Auto.modello = Modello.id_modello
AND Modello.costruttore = Costruttore.id_costruttore
AND Costruttore.casa_automobilistica = "Ford"
ORDER BY Auto.anno ASC;

/* Query 6 ESPLICITA: Elenco di tutti i modelli Ford, ordinate per anno */
\! echo "*** QUERY 6 - ESPLICITA ***"
SELECT Auto.anno, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Auto
JOIN Modello ON Auto.modello = Modello.id_modello
JOIN Costruttore ON Costruttore.id_costruttore = Modello.costruttore
WHERE Costruttore.casa_automobilistica = "Ford"
ORDER BY Auto.anno ASC;

/* Query 7 IMPLICITA: Elenco di tutte le auto Fiat immatricolate nel 2001 */
\! echo "*** QUERY 7 - IMPLICITA ***"
SELECT Auto.anno, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Auto, Modello, Costruttore
WHERE Auto.modello = Modello.id_modello
AND Modello.costruttore = Costruttore.id_costruttore
AND Costruttore.casa_automobilistica = "Fiat"
AND Auto.anno = 2001;

/* Query 7 ESPLICITA: Elenco di tutte le auto Fiat immatricolate nel 2001 */
\! echo "*** QUERY 7 - ESPLICITA ***"
SELECT Auto.anno, Modello.nome_modello, Costruttore.casa_automobilistica
FROM Auto
JOIN Modello ON Modello.id_modello = Auto.modello
JOIN Costruttore ON Costruttore.id_costruttore = Modello.costruttore
WHERE Costruttore.casa_automobilistica = "Fiat"
AND Auto.anno = 2001;

/* Query 8: Costo medio dei pezzi aventi descrizione “motore” */
\! echo "*** QUERY 8 ***"
SELECT Pezzo.nome, AVG(Pezzo.prezzo)
FROM Pezzo
WHERE Pezzo.nome = "Motore";

/* Query 9 IMPLICITA: Elenco delle date, prezzi e tipo di intervento effettuati dal cliente Bianchi */
\! echo "*** QUERY 9 - IMPLICITA ***"
SELECT Cliente.nome, Cliente.cognome, Intervento.data_intervento, Intervento.tipo_intervento, Intervento.prezzo
FROM Intervento, Cliente, Auto
WHERE Auto.cliente = Cliente.id_cliente
AND Auto.targa = Intervento.targa
AND Cliente.cognome = "Bianchi";

/* Query 9 ESPLICITA: Elenco delle date, prezzi e tipo di intervento effettuati dal cliente Bianchi */
\! echo "*** QUERY 9 - ESPLICITA ***"
SELECT Cliente.nome, Cliente.cognome, Intervento.data_intervento, Intervento.tipo_intervento, Intervento.prezzo
FROM Intervento
JOIN Auto ON Auto.targa = Intervento.targa
JOIN Cliente ON Auto.cliente = Cliente.id_cliente
WHERE Cliente.cognome = "Bianchi";

/* Query 10 IMPLICITA: Numero auto a cui è stata sostituita la marmitta */
\! echo "*** QUERY 10 - IMPLICITA ***"
SELECT Pezzo.nome, Auto.numero_auto
FROM Auto, Intervento, Utilizza, Pezzo
WHERE Auto.targa = Intervento.targa 
AND Intervento.id_intervento = Utilizza.intervento
AND Pezzo.id_pezzo = Utilizza.pezzo
AND Pezzo.nome = "Marmitta";

/* Query 10 ESPLICITA: Numero auto a cui è stata sostituita la marmitta */
\! echo "*** QUERY 10 - ESPLICITA ***"
SELECT Pezzo.nome, Auto.numero_auto
FROM Auto
JOIN Intervento ON Auto.targa = Intervento.targa
JOIN Utilizza ON Intervento.id_intervento = Utilizza.intervento
JOIN Pezzo ON Pezzo.id_pezzo = Utilizza.pezzo
WHERE Pezzo.nome = "Marmitta";