-- Galeasso Federico 5L 28/02/2024 - Modifiche Esami Studenti

use EsameStudenti;

INSERT INTO Esami VALUES (6, 'Analisi', 10, 'Aula 205', 'Lun-Mer 9-11');
INSERT INTO Studenti VALUES (9, 'Viola', 'Giulia', '2002-01-01', 'Corso X Maggio, 8', 'Analisi', 6);

UPDATE Esami SET Crediti = 15 WHERE Nome_Esame = 'Analisi';

REPLACE INTO Studenti (ID_studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame) 
VALUES (6, 'NuovoCognome', 'NuovoNome', '2000-01-01', 'NuovoIndirizzo', 'NuovoCorso', 2);

UPDATE Studenti SET Cognome = 'Marroni' WHERE ID_studente = 8;

UPDATE Studenti SET ID_Esame = 2 WHERE CorsoLaurea = 'Medicina';

UPDATE Esami SET Orario = 'Mar-Gio 08-10' WHERE Nome_Esame = 'Impianti elettrici';

UPDATE Esami SET Crediti = Crediti + 2 WHERE Nome_Esame = 'Sistemi Operativi';

UPDATE Studenti SET Cognome = 'Bianchi', Nome = 'Rosa', DataNascita = '1999-03-26', Indirizzo = 'Via Dante, 65', CorsoLaurea = 'Ingegneria Informatica', ID_Esame = 1 WHERE ID_studente = 5;

DELETE FROM Esami WHERE ID_Esame = 4;
-- ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`esamestudenti`.`studenti`, CONSTRAINT `studenti_ibfk_1` FOREIGN KEY (`ID_Esame`) REFERENCES `esami` (`ID_Esame`))

DELETE FROM Studenti WHERE ID_studente = 3;