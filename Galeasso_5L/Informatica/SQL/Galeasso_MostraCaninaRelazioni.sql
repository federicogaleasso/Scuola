-- Galeasso Federico 5L 1/2/2024 - Compito Mostra Canina SQL con Relazioni

CREATE DATABASE IF NOT EXISTS MostraCanina;

USE MostraCanina;

CREATE TABLE IF NOT EXISTS Proprietario(
    codFisc_p VARCHAR(16) NOT NULL,
    nome_p VARCHAR(45) NULL,
    cognome_p VARCHAR(45) NULL,
    indirizzo_p VARCHAR(45) NULL,
	telefono_p VARCHAR(10) NULL,
    PRIMARY KEY (codFisc_p)
);

CREATE TABLE IF NOT EXISTS Cane(
    id_c INT NOT NULL AUTO_INCREMENT,
	codFisc_p VARCHAR(16) NOT NULL,
    nome_c VARCHAR(45) NULL,
    dataNascita_c DATE NULL,
    altezza_c DECIMAL NULL,
	peso_c DECIMAL NULL,
    PRIMARY KEY (id_c),
	FOREIGN KEY(codFisc_p) REFERENCES Proprietario(codFisc_p)
);

CREATE TABLE IF NOT EXISTS Razza(
    id_r INT NOT NULL AUTO_INCREMENT,
	id_c INT NOT NULL,
    nome_r VARCHAR(45) NULL,
    altezza_r DECIMAL NULL,
	peso_r DECIMAL NULL,
    PRIMARY KEY (id_r),
	FOREIGN KEY(id_c) REFERENCES Cane(id_c)
);

CREATE TABLE IF NOT EXISTS Giudice(
    id_g INT NOT NULL AUTO_INCREMENT,
    nome_g VARCHAR(45) NULL,
	cognome_g VARCHAR(45) NULL,
    PRIMARY KEY (id_g)
);

CREATE TABLE IF NOT EXISTS Vota(
    id_g INT NOT NULL,
    codFisc_p VARCHAR(16) NOT NULL,
    votg INT NULL,
    FOREIGN KEY(id_g) REFERENCES Giudice(id_g),
    FOREIGN KEY(codFisc_p) REFERENCES Proprietario(codFisc_p)
);