<?php
    include './DB.php';

    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $tabella_utenti = "DROP TABLE IF EXISTS Utenti;";
		$tabella_post = "DROP TABLE IF EXISTS posts;";

        Database::collegati();
		if(Database::executeQuery($tabella_post) && Database::executeQuery($tabella_utenti)){
			echo "Tabelle eliminate con successo";
		} else{
			echo "Errore";
		}
	}
?>