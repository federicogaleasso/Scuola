<?php
    include './DB.php';

    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $tabella_utenti = "CREATE TABLE IF NOT EXISTS users (
			user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
			username VARCHAR(25) NOT NULL,
			email VARCHAR(25) NOT NULL
		);";

        $tabella_post = "CREATE TABLE IF NOT EXISTS posts (
			id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
			title VARCHAR(25) NOT NULL,
			content TEXT NOT NULL,
			user_id INT NOT NULL,
			FOREIGN KEY (user_id) REFERENCES users(user_id)
		);";

        Database::collegati();

        Database::executeQuery($tabella_utenti);
        Database::executeQuery($tabella_post);
        
	}
?>