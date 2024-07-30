<?php
session_start();

if (!isset($_SESSION['username'])) {
	header('Location: index.php');
	exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Benvenuto</title>
</head>
<body>

<h2>Benvenuto, <?php echo $_SESSION['username']; ?>!</h2>
<p>Questa è la pagina di benvenuto.</p>
<a href="index.php">Torna alla home page</a>

</body>
</html>