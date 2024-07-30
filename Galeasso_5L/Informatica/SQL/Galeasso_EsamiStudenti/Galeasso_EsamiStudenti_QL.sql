-- Galeasso Federico 5L 06/03/2024 - QL Esami Studenti

-- 1. Elenco di tutti gli Studenti
SELECT * FROM Studenti;

-- 2. Cognome e Nome di tutti gli studenti iscritti a Medicina
SELECT Cognome, Nome
FROM Studenti
WHERE CorsoLaurea = 'Medicina';

-- 3. Cognome, Indirizzo e Corso di Laurea degli studenti il cui nome inizia con "Mar"
SELECT Cognome, Indirizzo, CorsoLaurea
FROM Studenti
WHERE Nome LIKE 'Mar%';

-- 4. Nome e data di nascita di tutti gli studenti con Cognome Bianchi
SELECT Nome, DataNascita
FROM Studenti
WHERE Cognome = 'Bianchi';

-- 5. Elenco degli studenti ordinati per cognome
SELECT * FROM Studenti
ORDER BY Cognome ASC;

-- 6. Cognome, nome e indirizzo di tutti gli studenti nati tra il 1997 e 1999
SELECT Cognome, Nome, Indirizzo
FROM Studenti
WHERE DataNascita BETWEEN '1997-01-01' AND '1999-12-31';

-- 7. Cognome e nome degli studenti iscritti ad Economia abitanti in Corso Italia
SELECT Cognome, Nome
FROM Studenti
WHERE CorsoLaurea = 'Economia' AND Indirizzo = 'Corso Italia';

-- 8. Cognome e nome degli studenti che dovranno sostenere l'esame 1
SELECT Cognome, Nome
FROM Studenti
WHERE ID_Esame = 1;

-- 9. Elenco degli studenti ordinati per Corso di Laurea e successivamente per cognome
SELECT CorsoLaurea, Cognome, Nome
FROM Studenti
ORDER BY CorsoLaurea ASC, Cognome ASC;

-- 10. Elenco di tutti i dati della tabella Esami
SELECT * FROM Esami;

-- 11. Nome degli esami con credito maggiore di 9 (compreso)
SELECT Nome_Esame
FROM Esami
WHERE Crediti >= 9;

-- 12. Nome degli esami il cui orario è dalle 14 alle 16
SELECT Nome_Esame
FROM Esami
WHERE Orario BETWEEN '14:00' AND '16:00';