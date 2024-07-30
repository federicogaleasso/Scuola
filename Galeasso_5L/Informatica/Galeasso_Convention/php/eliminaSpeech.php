<?php
    include './database.php';
    session_start();
    Database::connessione();

    if(isset($_POST['idProgramma'])) {
        $idProgramma = $_POST['idProgramma'];
		$idSpeech = $_POST['idSpeech'];
		$nomeSala = $_POST['nomeSala'];

        $queryRecuperaNomeSala = "SELECT NomeSala FROM PROGRAMMA WHERE IDProgramma = $idProgramma";
        $risultatoNomeSala = Database::eseguiQuery($queryRecuperaNomeSala);

        $queryEliminaRelaziona = "DELETE FROM RELAZIONA WHERE IDProgramma = $idProgramma";
        Database::eseguiQuery($queryEliminaRelaziona);

        $queryEliminaSceglie = "DELETE FROM SCEGLIE WHERE IDProgramma = $idProgramma";
        Database::eseguiQuery($queryEliminaSceglie);

        $queryEliminaProgramma = "DELETE FROM PROGRAMMA WHERE IDProgramma = $idProgramma";
        Database::eseguiQuery($queryEliminaProgramma);

        $queryEliminaSala = "DELETE FROM SALA WHERE NomeSala = '$nomeSala'";
        Database::eseguiQuery($queryEliminaSala);

        $queryEliminaSpeech = "DELETE FROM SPEECH WHERE IDSpeech = $idSpeech";
        Database::eseguiQuery($queryEliminaSpeech);

        echo "Speech eliminato con successo";
        header("Refresh: 1, url=./portaleAdmin.php");
        exit();
    } else {
        echo "Errore";
    }
?>
