-- Galeasso Federico 5L 8/2/2024 - Compito Salone Del Gusto SQL

CREATE DATABASE IF NOT EXISTS SaloneDelGusto;

USE SaloneDelGusto;

CREATE TABLE IF NOT EXISTS Azienda (
   nomeAzienda VARCHAR(50) NOT NULL,
	PRIMARY KEY (nomeAzienda)
);

CREATE TABLE IF NOT EXISTS Stand (
	IDS INT NOT NULL AUTO_INCREMENT,
	nomeAzienda VARCHAR(50) NOT NULL,
	zona VARCHAR(20) NOT NULL,
	superficie INT NOT NULL,
	PRIMARY KEY (IDS),
	FOREIGN KEY (nomeAzienda) REFERENCES Azienda(nomeAzienda)
);

CREATE TABLE IF NOT EXISTS Visitatore (
	codiceV INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	eta INT NOT NULL,
	PRIMARY KEY (codiceV)
);

CREATE TABLE IF NOT EXISTS Prodotto (
   codiceP INT NOT NULL AUTO_INCREMENT,
	IDS INT NOT NULL,
	nomeAzienda VARCHAR(50) NOT NULL,
   caratteristiche VARCHAR(200) NOT NULL,
   tipologia VARCHAR(50) NOT NULL,
	PRIMARY KEY (codiceP),
	FOREIGN KEY (IDS) REFERENCES Stand(IDS),
   FOREIGN KEY (nomeAzienda) REFERENCES Azienda(nomeAzienda)
);

CREATE TABLE IF NOT EXISTS Assaggia (
    codiceV INT NOT NULL,
    codiceP INT NOT NULL,
    numeroAssaggi INT NOT NULL,
    PRIMARY KEY (codiceV,codiceP),
    FOREIGN KEY (codiceV) REFERENCES Visitatore(codiceV),
    FOREIGN KEY (codiceP) REFERENCES Prodotto(codiceP)
);
