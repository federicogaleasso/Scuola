<?php
    include './DB.php';

    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $tabella_utenti = "DROP TABLE IF EXISTS users;";
        $tabella_post = "DROP TABLE IF EXISTS posts;";

        Database::collegati();
		Database::executeQuery($tabella_post);
		Database::executeQuery($tabella_utenti);

	}
?>