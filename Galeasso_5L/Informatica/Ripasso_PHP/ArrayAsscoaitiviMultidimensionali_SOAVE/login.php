<?php
// Controlla se le variabili GET "user" e "password" sono impostate
if (isset($_GET["user"]) && isset($_GET["password"])) {
    // Recupera i valori da $_GET e assegnali a variabili locali
    $user = $_GET["user"];
    $pw = $_GET["password"];

    // Inizializza un array vuoto chiamato $database
    $database = array();

    // Popola l'array $database con dati fittizi per 5 utenti
    for ($utenti_db = 1; $utenti_db <= 5; $utenti_db++) {
        // Genera una password casuale per ogni utente
        $psw = rand($utenti_db, ($utenti_db + 1) * 5);
        // Aggiunge un array associativo con le informazioni dell'utente all'array $database
        $database[] = array(
            "user" => "utente" . $utenti_db,
            "password" => $psw,
            "passwordcrip" => md5($psw),
        );
    }

    // Inizializza una variabile $updated a false
    $updated = false;

    // Itera attraverso l'array $database per trovare l'utente corrispondente
    foreach ($database as $num => &$data) {
        if ($data["user"] == $user) {
            // Se l'utente è trovato, imposta la variabile $nc con l'indice dell'utente
            $nc = $num;
            $updated = true;
            break;
        }
    }

    // Se l'utente è stato trovato, aggiorna la password e mostra un messaggio
    if ($updated) {
        $database[$nc]["password"] = $pw;
        $database[$nc]["passwordcrip"] = md5($pw);
        echo "Password cambiata per l'utente: $user<br>";
        echo "<pre>";
        print_r($database[$nc]);
        echo "</pre>";
    } else {
        // Se l'utente non è stato trovato, mostra un messaggio di errore
        echo "Utente non trovato nel database.";
    }

    // Mostra l'intero array $database (con le nuove password)
    echo "<pre>";
    print_r($database);
    echo "</pre>";
}
// Se non sono presenti le variabili "user" e "password" e la variabile "invio" non è impostata
elseif (!isset($_GET["invio"])) {
    // Mostra un messaggio di accesso negato
    echo "<pre>";
    echo "<h1>accesso negato</h1>";
    echo "</pre>";
}
?>
