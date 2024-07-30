-- Galeasso Federico 5L 23/2/2024 - DML Merendine SQL

USE Merendine;

INSERT INTO Merende VALUES
	('ME1', 'Barretta di cioccolato', 1.50),
	('ME2', 'Caffè espresso', 0.80),
	('ME3', 'Acqua frizzante', 2.00);
	
INSERT INTO Scuole VALUES
	('S1', 'Scuola elementare'),
	('S2', 'Scuola media'),
	('S3', 'Scuola superiore');

INSERT INTO Macchinette VALUES
	('MA1', 'Snack', 'S1'),
	('MA2', 'Caffè', 'S2'),
	('MA3', 'Acqua', 'S3');

INSERT INTO Posizioni VALUES
	('P1',15,'ME1','MA1'),
	('P2',17,'ME2','MA3'),
	('P3',12,'ME3','MA3');
