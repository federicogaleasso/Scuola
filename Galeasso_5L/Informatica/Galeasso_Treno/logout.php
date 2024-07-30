<?php
session_start();
session_destroy();
setcookie('authenticated', '', time() - 3600); // Invalida il cookie
header('Location: index.php');
exit();
?>

