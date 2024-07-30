-- Galeasso Federico 5L 10/03/2024 - DML Dipendenti Dipartimenti

USE DipendentiDipartimenti;

INSERT INTO Dipartimenti  VALUES
	('Amm', 'Amministrazione', 'Roma', 12),
	('Amm1', 'Amministrazione', 'Torino', 10),
	('Amm2', 'Amministrazione', 'Milano', 12),
	('Direz', 'Direzione Generale', 'Roma', 4),
	('Mag', 'Magazzino', 'Torino', 10),
	('Mkt', 'Marketing', 'Milano', 12),
	('Prod', 'Produzione', 'Torino', 15),
	('R&S', 'Ricerca&Sviluppo', 'Torino', 20);

INSERT INTO Impiegati VALUES
	(1, 'Mario', 'Rossi', 'Torino', 3200, 'Prod'),
	(5, 'Marco', 'Viola', 'Palermo', 2830, 'Amm1'),
	(6, 'Enrico', 'Morenta', 'Torino', 2500, 'Mag'),
	(10, 'Margherita', 'Colombi', 'Roma', 6500, 'Prod'),
	(11, 'Fabrizio', 'Magenta', 'Torino', 4100, 'Prod'),
	(12, 'Franco', 'Volpi', 'Bari', 6100, 'Amm'),
	(13, 'Ugo', 'Boss', 'Cagliari', 8500, 'Direz'),
	(14, 'Mario', 'Gentili', 'Firenze', 5700, 'R&S'),
	(16, 'Elisabetta', 'Gregis', 'Roma', 2900, 'Amm'),
	(17, 'Laura', 'Moretti', 'Venezia', 5260, 'Mkt'),
	(18, 'Eirca', 'Bruni', 'Firenze', 6150, 'Mag'),
	(19, 'Anita', 'Bianco', 'Perugia', 3900, 'Direz'),
	(22, 'Federico', 'Felici', 'Milano', 4250, 'Amm2'),
	(23, 'Valentino', 'Menta', 'Firenze', 6255, 'Amm2');