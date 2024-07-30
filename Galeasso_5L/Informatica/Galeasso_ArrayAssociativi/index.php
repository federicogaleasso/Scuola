<!DOCTYPE html>
<html>
<head>
	<title>Galeasso - Array Associativi</title>
</head>
<body>
	<h1>Esempio di Array Associativo in PHP</h1>

	<?php
		// Definizione di un array associativo	
		$array = [
			'nome' => 'Mario', 
			'cognome' => 'Rossi', 
			'eta' => '20', 
			'lavoro' => 'Programmatore'
		];

		// Stampa degli elementi dell'array associativo
		echo "<p>Nome: " . $array['nome'] . "</p>";
		echo "<p>Cognome: " . $array['cognome'] . "</p>";
		echo "<p>Età: " . $array['eta'] . "</p>";
		echo "<p>Lavoro: " . $array['lavoro'] . "</p>";
		echo "<p>Email: " . $array['email'] . "</p>";
		echo "<br />";

		// Modifica di un elemento dell'array associativo
		$array['eta'] = 25;

		// Aggiunta di un nuovo elemento all'array associativo
		$array['email'] = 'mario.rossi@gmail.com';

		// Rimozione di un elemento dall'array associativo
		unset($array['lavoro']);
		
		echo "<h2>Stampa degli elementi dell'array associativo dopo aver eseguito le modifiche</h2>";
		echo "<p>Nome: " . $array['nome'] . "</p>";
		echo "<p>Cognome: " . $array['cognome'] . "</p>";
		echo "<p>Età: " . $array['eta'] . "</p>";
		echo "<p>Lavoro: " . $array['lavoro'] . "</p>";
		echo "<p>Email: " . $array['email'] . "</p>";
		echo "<br />";
		
		// Controlla se l'elemento con la chiave 'email' esiste nell'array associativo
		if (isset($array['email'])) {
			echo "<p>L'elemento <strong>Email</strong> è presente nell'array</p>";
		}
		?>
		
		<br />
		<h2>Cerca un valore nell'array</h2>
		<form action="" method="get">
			<input type="text" name="cerca" placeholder="Inserisci il valore da cercare">
			<input type="submit" value="Cerca">
		</form>
		
		<?php
		// Verifica se il valore cercato è presente nell'array associativo
		if (isset($_GET['cerca'])) {
			$valore_cercato = $_GET['cerca'];
			if (in_array($valore_cercato, $array)) {
				echo "<p> Il valore cercato <strong>" . $valore_cercato . "</strong> è presente nell'array</p>";
			} else {
				echo "<p> Il valore cercato <strong>" . $valore_cercato . "</strong> non è presente nell'array</p>";
			}
		}
	?>
	
</body>
</html>
