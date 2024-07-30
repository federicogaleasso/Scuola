<?php
session_start();

if (!isset($_SESSION['authenticated']) || !$_SESSION['authenticated']) {
	header('Location: index.php');
	exit();
}

if (isset($_POST['prezzo']) && isset($_POST['tipoTreno'])) {
	$prezzoInserito = floatval($_POST['prezzo']);
	$tipoTreno = $_POST['tipoTreno'];

	$sovrapprezzo = 0;

	switch ($tipoTreno) {
		case 'SecondaClasse':
		$sovrapprezzo = 7;
			break;
		case 'PrimaClasse':
		$sovrapprezzo = 12;
			break;
		case 'Premium':
		$sovrapprezzo = 18;
			break;
	}

	$prezzoTmp = $prezzoInserito * ($sovrapprezzo / 100);
	$prezzoTot = $prezzoInserito + $prezzoTmp;

	echo "Il prezzo totale del biglietto è di <b>$prezzoTot</b> euro e il treno utilizzato è il <b>$tipoTreno</b>.";
	echo '<br><a href="logout.php">Logout</a>';
	exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Prenotazione Biglietto</title>
</head>
<body>

<form action="prenotazione.php" method="post">
	<label for="prezzo">Prezzo Base:</label>
	<input type="text" id="prezzo" name="prezzo" required><br>

	<label for="tipoTreno">Tipo di treno:</label>
	<select id="tipoTreno" name="tipoTreno" required>
		<option value="Seconda Classe">Freccia rossa seconda classe</option>
		<option value="Prima Classe">Freccia rossa prima classe</option>
		<option value="Premium">Freccia rossa premium</option>
	</select><br>

	<button type="submit">Calcola</button>
</form>

</body>
</html>

