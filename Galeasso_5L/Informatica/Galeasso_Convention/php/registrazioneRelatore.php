<?php
	include './database.php';
	session_start();
	Database::connessione();

	if ($_SERVER['REQUEST_METHOD'] == 'POST') {

		$nome = $_POST["nome"];
		$cognome = $_POST["cognome"];
		$email = $_POST["email"];
		$password = hash("sha256", $_POST["password"]);
		$ragioneSocialeAzienda = $_POST['ragioneSocialeAzienda'];
		$indirizzoAzienda = $_POST['indirizzoAzienda'];
		$telefonoAzienda = $_POST['telefonoAzienda'];
		$titolo = $_POST['titolo'];
		$argomento = $_POST['argomento'];
		$fasciaOraria = $_POST['fasciaOraria'];
		$nomeSala = $_POST['nomeSala'];
		$numero = $_POST['numero'];
		$nPostiSala = $_POST['nPostiSala'];

		$existsUser = Database::eseguiQuery("SELECT * FROM UTENTE WHERE Email = '$email'")->fetch_assoc();
		$existsAzienda = Database::eseguiQuery("SELECT * FROM AZIENDA WHERE RagioneSocialeAzienda = '$ragioneSocialeAzienda' AND IndirizzoAzienda = '$indirizzoAzienda' AND TelefonoAzienda = '$telefonoAzienda'")->fetch_assoc();
		$existsRelatore = Database::eseguiQuery("SELECT * FROM RELATORE WHERE MailRel = '$email'")->fetch_assoc();
		$existsSpeech = Database::eseguiQuery("SELECT * FROM SPEECH WHERE Titolo = '$titolo' AND Argomento = '$argomento'")->fetch_assoc();
		$existsPiano = Database::eseguiQuery("SELECT * FROM PIANO WHERE Numero = '$numero'")->fetch_assoc();
		$existsSala = Database::eseguiQuery("SELECT * FROM SALA WHERE NomeSala = '$nomeSala' AND Numero = '$numero'")->fetch_assoc();
		$existsProgramma = Database::eseguiQuery("SELECT * FROM PROGRAMMA WHERE FasciaOraria = '$fasciaOraria' AND NomeSala = '$nomeSala'")->fetch_assoc();

		if (!$existsUser && !$existsAzienda && !$existsRelatore && !$existsSpeech && !$existsPiano && !$existsSala && !$existsProgramma) {

			$queryUtente = "INSERT INTO UTENTE (Email, Password, Ruolo) VALUES ('$email', '$password', 'Relatore')";
			$ris = Database::eseguiQuery($queryUtente);
			$idUt = Database::eseguiQuery("SELECT * FROM UTENTE WHERE Email = '$email' AND Password = '$password'")->fetch_assoc()['IDUtente'];

			$queryAzienda = "INSERT INTO AZIENDA (RagioneSocialeAzienda, IndirizzoAzienda, TelefonoAzienda) VALUES ('$ragioneSocialeAzienda', '$indirizzoAzienda', '$telefonoAzienda')";
			$risultatoAzienda = Database::eseguiQuery($queryAzienda);

			$queryRelatore = "INSERT INTO RELATORE (CognomeRel, MailRel, NomeRel, RagioneSocialeAzienda, IDUtente) VALUES ('$cognome', '$email', '$nome', '$ragioneSocialeAzienda', '$idUt')";
			$risultatoRelatore = Database::eseguiQuery($queryRelatore);

			$querySpeech = "INSERT INTO SPEECH (Titolo, Argomento) VALUES ('$titolo', '$argomento')";
			$risultatoSpeech = Database::eseguiQuery($querySpeech);
			$idSpeech = Database::eseguiQuery("SELECT * FROM SPEECH WHERE Titolo = '$titolo' AND Argomento = '$argomento'")->fetch_assoc()['IDSpeech'];

			$queryPiano = "INSERT INTO PIANO (Numero) VALUES ('$numero')";
			$risultatoPiano = Database::eseguiQuery($queryPiano);

			$querySala = "INSERT INTO SALA (NomeSala, NPostiSala, Numero) VALUES ('$nomeSala', '$nPostiSala', '$numero')";
			$risultatoSala = Database::eseguiQuery($querySala);

			$queryProgramma = "INSERT INTO PROGRAMMA (FasciaOraria, IDSpeech, NomeSala) VALUES ('$fasciaOraria', '$idSpeech', '$nomeSala')";
			$risultatoProgramma = Database::eseguiQuery($queryProgramma);
			$idProgramma = Database::eseguiQuery("SELECT * FROM PROGRAMMA WHERE FasciaOraria = '$fasciaOraria' AND IDSpeech = '$idSpeech' AND NomeSala = '$nomeSala'")->fetch_assoc()['IDProgramma'];

			$idRel = Database::eseguiQuery("SELECT * FROM RELATORE WHERE CognomeRel = '$cognome' AND MailRel = '$email' AND NomeRel = '$nome' AND RagioneSocialeAzienda = '$ragioneSocialeAzienda' AND IDUtente = '$idUt'")->fetch_assoc()['IDRel'];
			$queryRelaziona = "INSERT INTO RELAZIONA (IDRel, IDProgramma) VALUES ('$idRel', '$idProgramma')";
			$risultatoRelaziona = Database::eseguiQuery($queryRelaziona);

			echo "Relatore registrato";
			header('Refresh: 1, url=../index.html');
		} else {
			echo "Uno o più campi sono già presenti nel database. Registrazione annullata.";
			header('Refresh: 1, url=./portaleAdmin.php');
		}
	}
?>