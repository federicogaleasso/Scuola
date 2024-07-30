<?php
	include './database.php';
	session_start();
	Database::connessione();

	if ($_SERVER["REQUEST_METHOD"] == "POST") {

		if (isset($_POST['idProgramma']) && isset($_COOKIE['idPartecipante'])) {
			$idProgramma = $_POST['idProgramma'];
			$idPartecipante = $_COOKIE['idPartecipante'];

			$querySceglie = "INSERT INTO SCEGLIE (IDPart, IDProgramma) VALUES ('$idPartecipante','$idProgramma')";
			$risultatoSceglie = Database::eseguiQuery($querySceglie);

			echo "Iscritto";
			header('Refresh: 1, url=./partecipante.php');
		}
	}
?>
