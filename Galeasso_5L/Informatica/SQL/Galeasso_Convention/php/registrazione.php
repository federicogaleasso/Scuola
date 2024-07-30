<?php
    include './database.php';
	session_start();
	Database::connessione();

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $nome = $_POST["nome"];
        $cognome = $_POST["cognome"];
		$email = $_POST["email"];
		$password = hash("sha256", $_POST["password"]);

		$existsUser = Database::eseguiQuery("SELECT * FROM Utente WHERE Email = '$email'")->fetch_assoc();
		if (!$existsUser) {
			$queryUtente = "INSERT INTO Utente (Email,Password,Ruolo) VALUES ('$email','$password','Partecipante')";
			$ris = Database::eseguiQuery($queryUtente);

			$idUt = Database::eseguiQuery("SELECT * FROM Utente WHERE Email = '$email' AND Password = '$password'")->fetch_assoc()['IDUtente'];
			$queryPartecipante = "INSERT INTO Partecipante (IDUtente,NomePart,CognomePart,MailPart,TipologiaPart) VALUES ('$idUt','$nome','$cognome','$email','Partecipante')";
			$ris = Database::eseguiQuery($queryPartecipante);

			echo "Utente registrato";
			header('Refresh: 1, url=../index.html');
		} else{
			echo "Uno o più campi sono già presenti nel database. Registrazione annullata.";
			header('Refresh: 1, url=../html/registrazione.html');
		}

	}
?>