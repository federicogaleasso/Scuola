-- Galeasso Federico 5L 10/03/2024 - QL Dipendenti Dipartimenti

USE DipendentiDipartimenti;

\! echo "\n1. Cognome e nome dei dipendenti che abitano a Roma\n"
SELECT Cognome, Nome
FROM Impiegati
WHERE Residenza = "Roma";

\! echo "\n2. Cognome e Nome dei dipendenti che lavorano nel reparto Prod, ordinato per Cognome\n"
SELECT Cognome, Nome
FROM Impiegati
WHERE CodDip = "Prod"
ORDER BY Cognome;

\! echo "\n3. L’elenco di tutti i dipendenti che hanno residenza a Torino oppure Firenze\n"
SELECT * 
FROM Impiegati
WHERE Residenza = "Torino" 
OR Residenza = "Firenze";

\! echo "\n4. Cognome, Nome e dipartimento dei dipendenti con stipendio compreso tra 2800 e 4200\n"
SELECT Cognome, Nome, CodDip
FROM Impiegati
WHERE Stipendio BETWEEN 2800 AND 4200;

\! echo "\n5. Cognome e stipendio dei dipendenti che si chiamano Mario\n"
SELECT Cognome, Stipendio
FROM Impiegati
WHERE Nome = "Mario";

\! echo "\n6. Tutti i dati della tabella dipendenti ordinati per Dipartimento ed in seguito per Cognome\n"
SELECT *
FROM Impiegati
ORDER BY CodDip, Cognome;

\! echo "\n7. Elenco dei Dipartimenti con sede Torino\n"
SELECT *
FROM Dipartimenti
WHERE Sede = "Torino";

\! echo "\n8. Sede ed uffici dei dipartimenti che iniziano per 'M'\n"
SELECT Sede, Uffici
FROM Dipartimenti
WHERE CodDip LIKE 'M%';

\! echo "\n9. Dati dei dipendenti che hanno “ent” nel loro cognome\n"
SELECT *
FROM Impiegati
WHERE Cognome LIKE '%ent%';

\! echo "\n10. Dati dei dipartimenti che hanno gli uffici n.12 e n.15\n"
SELECT *
FROM Dipartimenti
WHERE Uffici = 12 
OR Uffici = 15;

\! echo "\n11. Cognome e Nome di tutti i dipendenti che fanno parte di Dipartimenti con sede a Milano\n"
SELECT Nome, Cognome
FROM Impiegati, Dipartimenti
WHERE Impiegati.CodDip = Dipartimenti.CodDip
AND Dipartimenti.Sede = 'Milano';

\! echo "\n12. Cognome, Nome, stipendio e Sede di tutti i dipendenti del Dipartimento Amministrazione\n"
SELECT Nome, Cognome, Stipendio, Dipartimenti.Sede
FROM Impiegati, Dipartimenti
WHERE Impiegati.CodDip = Dipartimenti.CodDip
AND Dipartimenti.Dipartimento = "Amministrazione";