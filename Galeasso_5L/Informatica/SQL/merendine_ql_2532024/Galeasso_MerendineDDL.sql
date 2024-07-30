CREATE DATABASE IF NOT EXISTS 5L_Merendine;
USE 5L_Merendine;

CREATE TABLE Merende(
	CodMerenda VARCHAR(5),
	NomeMerenda VARCHAR(20) NOT NULL,
	Prezzo FLOAT NOT NULL,
	PRIMARY KEY(CodMerenda));
	
CREATE TABLE Scuole(
	CodScuola VARCHAR(5),
	NomeScuola VARCHAR(20) NOT NULL,
	PRIMARY KEY(CodScuola));
	
CREATE TABLE Macchinette(
	CodMacchinetta VARCHAR(5),
	TipoMacchinetta VARCHAR(20) NOT NULL,
	CodSc VARCHAR(5),
	PRIMARY KEY(CodMacchinetta),
	FOREIGN KEY (CodSc) REFERENCES Scuole(CodScuola));
	
CREATE TABLE Posizioni(
	CodPos VARCHAR(5),
	QtaMerendine INT(6) NOT NULL,
	CodMer VARCHAR(5),
	CodMac VARCHAR(5),
	PRIMARY KEY(CodPos),
	FOREIGN KEY (CodMer) REFERENCES Merende(CodMerenda),
	FOREIGN KEY (CodMac) REFERENCES Macchinette(CodMacchinetta));
