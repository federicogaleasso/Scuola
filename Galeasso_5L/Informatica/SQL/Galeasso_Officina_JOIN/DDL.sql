-- Galeasso Federico 5L 14/04/2024 - Officina DDL

DROP DATABASE IF EXISTS Officina;

CREATE DATABASE IF NOT EXISTS Officina;

USE Officina;

CREATE TABLE IF NOT EXISTS Cliente(
    id_cliente VARCHAR(10) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    cognome VARCHAR(40) NOT NULL,
    via VARCHAR(40) NOT NULL,
    numero_via INT NOT NULL,
    cap INT NOT NULL,
    citta VARCHAR(40) NOT NULL,
    provincia VARCHAR(2) NOT NULL,
    PRIMARY KEY (id_cliente)
);

CREATE TABLE IF NOT EXISTS Costruttore(
    id_costruttore VARCHAR(30) NOT NULL,
    casa_automobilistica VARCHAR (30) NOT NULL,
    PRIMARY KEY(id_costruttore)
);

CREATE TABLE IF NOT EXISTS Modello(
    id_modello VARCHAR(30) NOT NULL,
    nome_modello VARCHAR(30) NOT NULL,
    anno INT NOT NULL,
    costruttore VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_modello),
    FOREIGN KEY (costruttore) REFERENCES Costruttore(id_costruttore)
);

CREATE TABLE IF NOT EXISTS Auto(
    targa VARCHAR(30) NOT NULL,
    anno INT NOT NULL,
    numero_auto INT NOT NULL,
    informazioni VARCHAR(30) NOT NULL,
    epoca VARCHAR(30) NOT NULL,
    modello VARCHAR(30) NOT NULL,
    cliente VARCHAR(10) NOT NULL,
    PRIMARY KEY (targa),
    FOREIGN KEY (modello) REFERENCES Modello(id_modello),
    FOREIGN KEY (cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS Pezzo(
    id_pezzo VARCHAR(30) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    prezzo FLOAT NOT NULL,
    PRIMARY KEY (id_pezzo)
);

CREATE TABLE IF NOT EXISTS Intervento(
    id_intervento VARCHAR(15) NOT NULL,
    tipo_intervento VARCHAR(50),
    data_intervento DATE NOT NULL,
    prezzo FLOAT NOT NULL,
    targa VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_intervento),
    FOREIGN KEY (targa) REFERENCES Auto(targa)
);

CREATE TABLE IF NOT EXISTS Utilizza(
    intervento VARCHAR(15) NOT NULL,
    pezzo VARCHAR(30) NOT NULL,
    FOREIGN KEY (pezzo) REFERENCES Pezzo(id_pezzo),
    FOREIGN KEY (intervento) REFERENCES Intervento(id_intervento)
);