<?php
session_start();

$utenti = [
	'ut1' => ['pw1', ''],
	'ut2' => ['pw2', ''],
	'ut3' => ['pw3', '']
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$username = $_POST['username'];
	$password = $_POST['password'];
	$colore = $_POST['colore'];

	if (isset($utenti[$username]) && $utenti[$username][0] === $password) {
		$_SESSION['username'] = $username;

		setcookie($username . '_colore', $colore, time() + 120, "/");

		header('Location: benvenuto.php');
		exit();
	} else {
		echo 'Login fallito. Riprova.';
	}
}
?>