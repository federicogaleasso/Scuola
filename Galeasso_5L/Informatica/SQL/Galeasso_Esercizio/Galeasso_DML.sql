USE Esercizio;

INSERT INTO film (anno,trama,linktrailer,titolo,durata) VALUES
	('2000','TramaFilm1','www.linkfilm1.com','Film1',150),
	('2005','TramaFilm2','www.linkfilm2.com','Film2',120),
	('2020','TramaFilm3','www.linkfilm3.com','Film3',190),
	('2017','TramaFilm4','www.linkfilm4.com','Film4',100),
	('2008','TramaFilm5','www.linkfilm5.com','Film5',125);

INSERT INTO utente (username,password,nome,indirizzo,email) VALUES
	('mario5','c7932f498667cb7369a9ead8078dd5ecc647dfcb2aaf172bc54be232cbc0c4ce','Mario','Via Blu','mario@gmail.com'),
	('luca10','7d5db98ae719b7c1c12cc3134c5815b17a187e84858a80f82ae5d82f9e7d9b75','Luca','Via Verde','luca@gmail.com'),
	('paolo15','3788ad4f1a2389a0b7edf43952c8b121df0666a92b7c477d50f785c9c299db5c','Paolo','Via Rosso','paolo@gmail.com');

INSERT INTO attore (nome,datanascita) VALUES
	('Attore1','1980-12-05'),
	('Attore2','1985-04-23'),
	('Attore3','1990-10-15');
	
INSERT INTO visualizza (data,id_film,id_utente) VALUES
	('2024-12-05',1,2),
	('2024-10-13',2,3),
	('2024-02-22',3,1),
	('2024-11-15',4,2),
	('2024-01-15',5,3);
	
INSERT INTO interpretato (id_film,id_attore) VALUES
	(1,2),
	(2,3),
	(3,1),
	(4,2),
	(5,3);
