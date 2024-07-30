-- Galeasso Federico 5L - Convention DML

USE Galeasso_Convention;

INSERT INTO UTENTE (Email, Password, Ruolo) VALUES
('admin@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Admin'),
('mariorossi@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('lucaverdi@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('alessandroferrari@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('francescorusso@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('paoloesposito@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('mattiabianchi@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('lorenzoromano@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('federicogallo@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('leonardocosta@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('andreafontana@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Relatore'),
('riccardoconti@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('tommasoricci@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('gabrielebruno@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('fabriziodeluca@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('flavianomoretti@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('matteomarino@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('giuseppegreco@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('diegobaribieri@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('nicololombardi@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante'),
('edoardogiordano@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Partecipante');

INSERT INTO AZIENDA (RagioneSocialeAzienda, IndirizzoAzienda, TelefonoAzienda) VALUES
('Azienda1', 'IndirizzoAzienda1', '1234567890'),
('Azienda2', 'IndirizzoAzienda2', '0987654321'),
('Azienda3', 'IndirizzoAzienda3', '9876543210'),
('Azienda4', 'IndirizzoAzienda4', '0123456789'),
('Azienda5', 'IndirizzoAzienda5', '1112223333'),
('Azienda6', 'IndirizzoAzienda6', '4445556666'),
('Azienda7', 'IndirizzoAzienda7', '7778889999'),
('Azienda8', 'IndirizzoAzienda8', '0001112222'),
('Azienda9', 'IndirizzoAzienda9', '3334445555'),
('Azienda10', 'IndirizzoAzienda10', '6667778888');

INSERT INTO RELATORE (CognomeRel, mailRel, NomeRel, RagioneSocialeAzienda, IDUtente) VALUES
('Rossi', 'mariorossi@gmail.com', 'Mario', 'Azienda1', 2),
('Verdi', 'lucaverdi@gmail.com', 'Luca', 'Azienda2', 3),
('Ferrari', 'alessandroferrari@gmail.com', 'Alessandro', 'Azienda3', 4),
('Russo', 'francescorusso@gmail.com', 'Francesco', 'Azienda4', 5),
('Esposito', 'paoloesposito@gmail.com', 'Paolo', 'Azienda5', 6),
('Bianchi', 'mattiabianchi@gmail.com', 'Mattia', 'Azienda6', 7),
('Romano', 'lorenzoromano@gmail.com', 'Lorenzo', 'Azienda7', 8),
('Gallo', 'federicogallo@gmail.com', 'Federico', 'Azienda8', 9),
('Costa', 'leonardocosta@gmail.com', 'Leonardo', 'Azienda9', 10),
('Fontana', 'andreafontana@gmail.com', 'Andrea', 'Azienda10', 11);

INSERT INTO PIANO (Numero) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10);

INSERT INTO SALA (NomeSala, NpostiSala, Numero) VALUES
('Sala 1', 50, 1),
('Sala 2', 40, 2),
('Sala 3', 30, 3),
('Sala 4', 20, 4),
('Sala 5', 10, 5),
('Sala 6', 50, 6),
('Sala 7', 40, 7),
('Sala 8', 30, 8),
('Sala 9', 20, 9),
('Sala 10', 10, 10);

INSERT INTO PARTECIPANTE (CognomePart, NomePart, MailPart, TipologiaPart, IDUtente) VALUES
('Conti', 'Riccardo', 'riccardoconti@gmail.com', 'Partecipante', 12),
('Ricci', 'Tommaso', 'tommasoricci@gmail.com', 'Partecipante', 13),
('Bruno', 'Gabriele', 'gabrielebruno@gmail.com', 'Partecipante', 14),
('De Luca', 'Fabrizio', 'fabriziodeluca@gmail.com', 'Partecipante', 15),
('Moretti', 'Flaviano', 'flavianomoretti@gmail.com', 'Partecipante', 16),
('Marino', 'Matteo', 'matteomarino@gmail.com', 'Partecipante', 17),
('Greco', 'Giuseppe', 'giuseppegreco@gmail.com', 'Partecipante', 18),
('Barbieri', 'Diego', 'diegobaribieri@gmail.com', 'Partecipante', 19),
('Lombardi', 'Nicolò', 'nicololombardi@gmail.com', 'Partecipante', 20),
('Giordano', 'Edoardo', 'edoardogiordano@gmail.com', 'Partecipante', 21);

INSERT INTO SPEECH (Titolo, Argomento) VALUES
('Sicurezza', 'Protezione'),
('IA', 'Applicazioni'),
('Catena', 'Utilizzi'),
('IoT', 'Efficienza'),
('Sviluppo', 'Tecnologie'),
('Dati', 'Gestione'),
('Cloud', 'Vantaggi'),
('Apprendimento', 'Concetti'),
('Collaborazione', 'Cultura'),
('Consapevolezza', 'Educazione');

INSERT INTO PROGRAMMA (FasciaOraria, IDSpeech, NomeSala) VALUES
('Lun 07:00-08:00', 1, 'Sala 1'),
('Lun 09:00-10:00', 2, 'Sala 2'),
('Lun 11:00-12:00', 3, 'Sala 3'),
('Mar 07:30-08:30', 4, 'Sala 4'),
('Mar 9:30-10:30', 5, 'Sala 5'),
('Mar 11:30-12:30', 6, 'Sala 6'),
('Mer 12:30-13:30', 7, 'Sala 7'),
('Mer 14:30-15:30', 8, 'Sala 8'),
('Mer 17:30-18:30', 9, 'Sala 9'),
('Ven 16:30-17:30', 10, 'Sala 10');

INSERT INTO RELAZIONA (IDRel, IDProgramma) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO SCEGLIE (IDPart, IDProgramma) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);