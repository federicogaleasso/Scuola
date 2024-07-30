<?php
	$studenti = array(
		"Rossi" => array(
			"nome" => "Mario",
			"italiano" => 8,
			"storia" => 6.5,
			"matematica" => 7,
			"inglese" => 6,
			"scienze" => 8
		),
		"Gallo" => array(
			"nome" => "Luca",
			"italiano" => 7,
			"storia" => 5,
			"matematica" => 9,
			"inglese" => 7,
			"scienze" => 10
		),
		"Esposito" => array(
			"nome" => "Francesco",
			"italiano" => 7,
			"storia" => 9,
			"matematica" => 2.5,
			"inglese" => 7,
			"scienze" => 4.5
		),
		"Ferrari" => array(
			"nome" => "Anna",
			"italiano" => 6,
			"storia" => 5,
			"matematica" => 10,
			"inglese" => 10,
			"scienze" => 6.5
		),
	);

	$cognome = $_POST['cognome'];

	if (array_key_exists($cognome, $studenti)) {
		$materia = $_POST['materia'];

		$nome = $studenti[$cognome]['nome'];
		$valutazione = $studenti[$cognome][$materia];

		echo "Nome dello studente: <b>$nome</b><br>";
		echo "Voto di <i>$materia</i>: <b>$valutazione</b>";
		echo "<br/><br/><a href='index.html'>Cerca altri studenti</a>";
	} else {
		echo "Cognome non trovato.<br/><br/><a href='index.html'>Riprova con un altro cognome</a>";
	}
?>
