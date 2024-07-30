-- Galeasso Federico 5L 25/02/2024 - CSV Viaggi SQL

USE Viaggi;

LOAD DATA INFILE './Galeasso_ViaggiCSV/Destinazioni.csv' INTO TABLE Destinazioni FIELDS TERMINATED BY ',' IGNORE 1 LINES (CodDest, Denominazione, Moneta);

LOAD DATA INFILE './Galeasso_ViaggiCSV/Clienti.csv' INTO TABLE Clienti FIELDS TERMINATED BY ',' IGNORE 1 LINES (CodCli, CognomeCli, NomeCli, IndirizzoCli, TelCli);

LOAD DATA INFILE './Galeasso_ViaggiCSV/TourOperator.csv' INTO TABLE TourOperator FIELDS TERMINATED BY ',' IGNORE 1 LINES (CodTour, NomeTour, IndirizzoTour, TelTour);

LOAD DATA INFILE './Galeasso_ViaggiCSV/Pacchetti.csv' INTO TABLE Pacchetti FIELDS TERMINATED BY ',' IGNORE 1 LINES (CodPacch, Modalita, Prezzo, CodDest, CodTour);

LOAD DATA INFILE './Galeasso_ViaggiCSV/Acquisti.csv' INTO TABLE Acquisti FIELDS TERMINATED BY ',' IGNORE 1 LINES (CodAcq, CodCli, CodPacch, DataAcquisto);