<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Login</title>
</head>
<body>

	<?php
		session_start();

		if (isset($_POST['username']) && isset($_POST['password'])) {
			$username = $_POST['username'];
			$password = $_POST['password'];

			if ($username === 'guest' && $password === '1234') {
				$_SESSION['authenticated'] = true;
				setcookie('authenticated', true, time() + 120); // Cookie con durata di 2 minuti
				header('Location: prenotazione.php');
				exit();
			} else {
				echo '<p>Nome utente o password errati.</p>';
			}
		}
	?>

	<form action="index.php" method="post">
		<label for="username">Username:</label>
		<input type="text" id="username" name="username" required><br>

		<label for="password">Password:</label>
		<input type="password" id="password" name="password" required><br>

		<button type="submit">Login</button>
	</form>

</body>
</html>

