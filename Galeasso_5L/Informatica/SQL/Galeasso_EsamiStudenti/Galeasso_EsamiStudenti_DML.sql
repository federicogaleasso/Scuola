-- Galeasso Federico 5L 26/02/2024 - DML Esami Studenti

USE EsameStudenti;

INSERT INTO Esami (ID_Esame, Nome_Esame, Crediti, Aula, Orario) VALUES
	(1, 'Sistemi Operativi', 6, 'Aula 101', 'Lun-Gio 10-12'),
	(2, 'Biologia Molecolare', 8, 'Aula 203', 'Mar-Ven 14-16'),
	(3, 'Economia Internazionale', 10, 'Aula Magna', 'Lun-Mer 16-18'),
	(4, 'Progettazione Architetture', 9, 'Aula Design', 'Mer-Gio 14-16'),
	(5, 'Impianti elettrici', 8, 'Aula 201', 'Lun-Gio 9-11');

INSERT INTO Studenti (ID_studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame) VALUES
	(1, 'Rossi', 'Marco', '1998-05-15', 'Via Roma, 123', 'Ingegneria Elettrica', 5),
	(2, 'Bianchi', 'Laura', '1999-08-22', 'Via Milano, 456', 'Medicina', 4),
	(3, 'Verdi', 'Luca', '1997-12-10', 'Corso Italia, 78', 'Economia', 3),
	(4, 'Neri', 'Chiara', '2000-03-03', 'Viale Europa, 5', 'Architettura', 4),
	(5, 'Bianchi', 'Rosa', '1999-03-26', 'Via Dante, 65', 'Ingegneria Informatica', 1),
	(6, 'Gialli', 'Marta', '1997-12-23', 'Corso Italia, 3', 'Medicina', 1),
	(7, 'Arancioni', 'Fabio', '1998-10-04', 'Via Roma, 31', 'Medicina', 3),
	(8, 'Verdoni', 'Carlo', '2000-02-02', 'Corso XXV Aprile, 4', 'Ingegneria Informatica', 1);