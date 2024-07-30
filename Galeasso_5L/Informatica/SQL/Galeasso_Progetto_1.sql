-- Galeasso Federico 5L 26/1/2024 - SQL

-- http://localhost/phpmyadmin/
-- ./mysql -u root
-- ./mysql -u root < ~/Documenti/INFO_5L/mysql/NomeFile.sql -t (con -t alla fine fa la stampa formattata)

-- Cancella il db
DROP database nuovodb;

-- Se non esiste lo crea, se esiste no
CREATE DATABASE IF NOT EXISTS nuovodb;

-- Mostra i database
SHOW DATABASE;

-- Serve per selezionare nel database
USE DATABASES;

-- Serve per creare la tabella
CREATE TABLE IF NOT EXISTS Persone(
    id INT NOT NULL AUTO_INCREMENT, -- Chiave primaria, che sicuramente non dovrà essere nulla (NOT NULL)
    nome CHAR(45) NULL, -- Questo campo può anche essere vuoto, perchè c'è NULL
    cognome VARCHAR(45) NULL,
    dataDiNascita DATE NULL,
    sesso ENUM('M','F') NULL, -- ENUM permette solo la scelta di quei caratteri
    PRIMARY KEY (id) -- Specifica la chiave primaria
);

-- NB
-- CHAR occuperà sempre tutti i posti anche se la parola sarà di 2.
-- VARCHAR ne occuperà il minimo indispensabile. VARCHAR utilizza più risorse, costa di più.

-- Mostra le tabelle
SHOW tables;

-- Mostra la struttura della tabella
DESCRIBE Persone;

-- Permette di mofificare la tabella
ALTER TABLE Persone;

-- Permette di rinominare la tabella
ALTER TABLE Persone RENAME Alunni;

-- Permette di cambiare un campo
ALTER TABLE Alunni CHANGE nome nome VARCHAR(50);

-- Permette di aggiungere un campo
ALTER TABLE Alunni ADD Indirizzo VARCHAR(25) NOT NULL;

-- Permette di eliminare un campo
ALTER TABLE Alunni DROP Indirizzo;

/*
Sono un commento
*/

-- Sono un commento

-- Stampa
\! echo "Ciao!"

 -- Permette di vedere il codice SQL di come creare una determinata tabella
SHOW CREATE TABLE Alunni
