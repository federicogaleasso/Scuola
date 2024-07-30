<?php
session_start();

session_unset();
session_destroy();

// setcookie('_colore', '', time() - 3600);
foreach ($_COOKIE as $key => $value) {
	setcookie($key, '', time() - 3600, '/');
}

header('Location: index.php');
exit();
?>