<?php
    include './DB.php';

    if($_SERVER['REQUEST_METHOD'] == "POST"){
        $nome_utente = $_POST['nome_utente'];
        $email_utente = $_POST['email_utente'];

        $inserisci_utente = "INSERT INTO users (username, email) VALUES ('$nome_utente', '$email_utente');";

        Database::collegati();

        if(Database::executeQuery($inserisci_utente)){
            echo "Utente inserito con successo!";
        } else {
            echo "Errore nell'inserimento dell'utente!";
        }

    }
?>