<?php
	include './database.php';
	session_start();
	Database::connessione();

	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		$email = $_POST["email"];
		$password = hash("sha256", $_POST["password"]);

		$query = "SELECT * FROM UTENTE WHERE Email=? AND Password=?";

		$stmt = Database::$connection->prepare($query);
		$stmt->bind_param("ss", $email, $password);
		$stmt->execute();
		$risultato = $stmt->get_result();

		if ($risultato->num_rows > 0) {
			$ruolo = Database::eseguiQuery(" SELECT * FROM UTENTE WHERE Email = '$email' AND Password = '$password';")->fetch_assoc()['Ruolo'];
			switch ($ruolo) {
				case 'Admin':
					header('Location: ./portaleAdmin.php');
					break;
				case 'Relatore':
					$idRelatore = Database::eseguiQuery("SELECT IDRel FROM RELATORE WHERE MailRel = '$email'")->fetch_assoc()['IDRel'];
					setcookie("idRelatore", $idRelatore, time() + 3600, "/");
					header('Location: ./relatore.php');
					break;
				case 'Partecipante':
					$idPartecipante = Database::eseguiQuery("SELECT IDPart FROM PARTECIPANTE WHERE MailPart = '$email'")->fetch_assoc()['IDPart'];
					setcookie("idPartecipante", $idPartecipante, time() + 3600, "/");
					header("Location: ./partecipante.php");
					break;
				default:
					echo "Errore nel login";
					header('Refresh: 1, url=../index.html');
			}
		} else{
			echo "Utente non trovato o credenziali errate";
			header('Refresh: 1, url=../index.html');
		}
	}
?>