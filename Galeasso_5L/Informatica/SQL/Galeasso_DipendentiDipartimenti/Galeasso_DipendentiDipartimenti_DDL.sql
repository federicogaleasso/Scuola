-- Galeasso Federico 5L 10/03/2024 - DDL Dipendenti Dipartimenti

CREATE DATABASE IF NOT EXISTS DipendentiDipartimenti;
USE DipendentiDipartimenti;

CREATE TABLE IF NOT EXISTS Dipartimenti(
    CodDip VARCHAR(50) NOT NULL,
    Dipartimento VARCHAR(50) NOT NULL,
    Sede VARCHAR(25) NOT NULL,
    Uffici INT NOT NULL,
    PRIMARY KEY(CodDip)
);

CREATE TABLE IF NOT EXISTS Impiegati(
    IDImpiegato INT NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    Residenza VARCHAR(20) NOT NULL,
    Stipendio INT NOT NULL,
    CodDip VARCHAR(50) NOT NULL,
    PRIMARY KEY(IDImpiegato),
    FOREIGN KEY(CodDip) REFERENCES Dipartimenti(CodDip)
);