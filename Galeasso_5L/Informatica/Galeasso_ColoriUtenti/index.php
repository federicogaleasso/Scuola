<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Home Page</title>
</head>
<body>

<?php
if (isset($_SESSION['username'])) {
	echo "<p>Ciao {$_SESSION['username']}, sei nella home page.</p>";

	if (isset($_COOKIE[$_SESSION['username'] . '_colore'])) {
		echo "<p>Il tuo colore preferito è {$_COOKIE[$_SESSION['username'] . '_colore']}.</p>";
	}

	echo '<a href="logout.php">Logout</a>';
} else {
	echo '
	<h2>Form di Autenticazione</h2>
	<form action="authenticate.php" method="post">
		<label for="username">Username:</label>
		<input type="text" id="username" name="username" required><br>

		<label for="password">Password:</label>
		<input type="password" id="password" name="password" required><br>

		<label for="colore">Colore preferito:</label>
		<input type="text" id="colore" name="colore" required><br>

		<input type="submit" value="Login">
	</form>';
}
?>

</body>
</html>