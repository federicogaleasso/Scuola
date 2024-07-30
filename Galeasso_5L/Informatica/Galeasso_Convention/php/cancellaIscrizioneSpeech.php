<?php
	include './database.php';
	session_start();
	Database::connessione();

	if ($_SERVER["REQUEST_METHOD"] == "POST") {

		if (isset($_POST['idProgramma']) && isset($_COOKIE['idPartecipante'])) {
			$idProgramma = $_POST['idProgramma'];
			$idPartecipante = $_COOKIE['idPartecipante'];

			$queryCancellaIscrizione = "DELETE FROM SCEGLIE WHERE IDPart = '$idPartecipante' AND IDProgramma = '$idProgramma'";
			$risultatoCancellaIscrizione = Database::eseguiQuery($queryCancellaIscrizione);

			echo "Iscrizione cancellata";
			header('Refresh: 1, url=./partecipante.php');
		} else {
            echo "Si è verificato un errore durante la cancellazione dell'iscrizione";
        }
	}
?>
