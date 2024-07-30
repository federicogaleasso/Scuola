<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nome = $_POST["nome"];
    $giorni = $_POST["giorni"];
    $orari = $_POST["orari"];

    $persone = [
        "nome" => $nome,
        "giorni" => $giorni,
        "orari" => $orari
    ];

    $_SESSION["persone"][] = $persone;

	?>

		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Dati inseriti</title>
		</head>
		<body>
			<h1>Dati inseriti</h1>

			<?php
			if (isset($_SESSION["persone"]) && !empty($_SESSION["persone"])) {
				foreach ($_SESSION["persone"] as $persona) {
					echo "<p><strong>Nome:</strong> " . $persona["nome"] . "</p>";
					echo "<p><strong>Giorno:</strong> " . $persona["giorni"] . "</p>";
					echo "<p><strong>Orario:</strong> " . $persona["orari"] . "</p>";
					echo "<hr>";
				}
			} else {
				echo "<p>Nessun dato disponibile.</p>";
			}
			?>

			<a href="index.php">Nuovo inserimento</a><br/>
			<a href="riepilogo.php">Elabora</a><br/>
			<a href="logout.php">Logout</a>
		</body>
		</html>

	<?php
}
?>