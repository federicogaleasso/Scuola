<?php
    include './DB.php';

    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $id_utente = $_POST['id_utente'];
        $titolo_post = $_POST['titolo_post'];
        $contenuto_post = $_POST['contenuto_post'];

        $inserisci_post = "INSERT INTO posts (username, title, content) VALUES ('$id_utente', '$titolo_post', '$contenuto_post');";

        Database::collegati();

        if(Database::executeQuery($inserisci_post)){
            echo "Post inserito con successo!";
        } else {
            echo "Errore nell'inserimento del post!";
        }

	}
?>