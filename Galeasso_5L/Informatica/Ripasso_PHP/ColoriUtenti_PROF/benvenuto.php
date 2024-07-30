<?php
    // Controlla se l'array associativo $_COOKIE contiene la chiave 'nomeu'
	if (array_key_exists('nomeu', $_COOKIE)) {
		// Se la chiave 'nomeu' è presente nei cookie, mostra un messaggio di benvenuto con il valore associato a 'nomeu'
		echo "Benvenuto utente " . $_COOKIE['nomeu'] . "<br>";
	}

    // Inizia o ripristina la sessione PHP
	session_start();
    
    // Controlla se l'array associativo $_SESSION contiene la chiave 'Snomeu'
	if (array_key_exists('Snomeu', $_SESSION)) {
		// Se la chiave 'Snomeu' è presente nella sessione, mostra un messaggio di benvenuto con il valore associato a 'Snomeu'
		echo "Benvenuto utente " . $_SESSION['Snomeu'] . " dalla sessione!<br>";
	}
?>
