<?php
    include './DB.php';
	
    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $tabella_utenti = "CREATE TABLE IF NOT EXISTS Utenti (
			username varchar(25) NOT NULL PRIMARY KEY, 
			password char(64) NOT NULL,
			last_login date DEFAULT NULL);";

		$popola_tb_utenti = "INSERT INTO Utenti (username, password, last_login) VALUES
		('federico', 'e24b8583baee347aefb33e88f1ff2549314ba4c9e7b85f2f43e781471bb296b6', '2024-04-18'),
		('luca', 'e24b8583baee347aefb33e88f1ff2549314ba4c9e7b85f2f43e781471bb296b6', '2024-04-18'),
		('paolo', 'e24b8583baee347aefb33e88f1ff2549314ba4c9e7b85f2f43e781471bb296b6', '2024-04-18');";

		$tabella_post = "CREATE TABLE IF NOT EXISTS posts (
			id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
			title VARCHAR(25) NOT NULL,
			content TEXT NOT NULL,
			username varchar(25) NOT NULL,
			FOREIGN KEY (username) REFERENCES Utenti(username)
		);";

        Database::collegati();
        if(Database::executeQuery($tabella_utenti) && Database::executeQuery($popola_tb_utenti) && Database::executeQuery($tabella_post)){
			echo "Tabelle create con successo";
		} else{
			echo "Errore";
		}        
	}
?>