DROP DATABASE IF EXISTS Esercizio;
CREATE DATABASE IF NOT EXISTS Esercizio;
USE Esercizio;

CREATE TABLE IF NOT EXISTS film (
	id_film INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	anno YEAR NOT NULL,
	trama TEXT NOT NULL,
	linktrailer VARCHAR(50) NOT NULL,
	titolo VARCHAR(25) NOT NULL,
	durata INT NOT NULL
);

CREATE TABLE IF NOT EXISTS utente (
	id_utente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(25) NOT NULL,
	password VARCHAR(64) NOT NULL,
	nome VARCHAR(25) NOT NULL,
	indirizzo VARCHAR(20) NOT NULL,
	email VARCHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS attore (
	id_attore INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(25) NOT NULL,
	datanascita DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS visualizza (
	data DATE NOT NULL,
	id_film INT NOT NULL,
	id_utente INT NOT NULL,
	FOREIGN KEY (id_film) REFERENCES film(id_film),
	FOREIGN KEY (id_utente) REFERENCES utente(id_utente),
	PRIMARY KEY(id_film,id_utente)
);

CREATE TABLE IF NOT EXISTS interpretato (
	id_film INT NOT NULL,
	id_attore INT NOT NULL,
	FOREIGN KEY (id_film) REFERENCES film(id_film),
	FOREIGN KEY (id_attore) REFERENCES attore(id_attore),
	PRIMARY KEY(id_film,id_attore)
);
