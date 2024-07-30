-- Galeasso Federico 5L 26/02/2024 - DDL Esami Studenti

CREATE DATABASE IF NOT EXISTS EsameStudenti;
USE EsameStudenti;

CREATE TABLE IF NOT EXISTS Esami (
    ID_Esame INT NOT NULL,
    Nome_Esame VARCHAR(50) NOT NULL,
    Crediti INT NOT NULL,
    Aula VARCHAR(10) NOT NULL,
    Orario VARCHAR(50) NOT NULL,
    PRIMARY KEY(ID_Esame)
);

CREATE TABLE IF NOT EXISTS Studenti (
    ID_studente INT NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    DataNascita DATE NOT NULL,
    Indirizzo VARCHAR(255) NOT NULL,
    CorsoLaurea VARCHAR(50) NOT NULL,
    ID_Esame INT NOT NULL,
    PRIMARY KEY(ID_studente),
    FOREIGN KEY(ID_Esame) REFERENCES Esami(ID_Esame)
);