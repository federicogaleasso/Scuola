<?php
    // Includi il file enable_debug.php che potrebbe contenere configurazioni per il debug
    include "./enable_debug.php";

    // Richiedi il file data.php che potrebbe contenere dati utilizzati nel codice
    require "./data.php";

    // Inizializza la variabile $err_msg a null
    $err_msg = null;

    // Definisci una funzione di salvataggio con parametri tipizzati
    $save = function (string $nome, array $giorni, array $fascia) use ($h_map, $day_map) {
        // Inizia o ripristina una sessione PHP
        session_start();

        // Se la variabile di sessione "day" non è impostata
        if (!isset($_SESSION["day"])) {
            // Inizializza la variabile di sessione "day" con array vuoti
            $_SESSION["day"] = array_combine($day_map, array_fill(0, count($day_map), []));

            // Inizializza gli array interni per ogni giorno
            foreach ($_SESSION["day"] as &$day) {
                $day = array_combine($h_map, array_fill(0, count($h_map), []));
            }

            // Debug: Stampa la variabile di sessione e interrompi l'esecuzione
            echo "<p><pre>";
            print_r($_SESSION);
            echo "</pre></p>";
            // exit();
        }

        // Aggiungi il nome nelle fasce orarie e giorni specificati
        foreach ($giorni as $giorno) {
            foreach ($fascia as $f) {
                $_SESSION["day"][$day_map[$giorno]][$h_map[$f]][] = $nome;
                $_SESSION["day"][$day_map[$giorno]][$h_map[$f]] = array_unique($_SESSION["day"][$day_map[$giorno]][$h_map[$f]]);
            }
        }
    };

    // Se la variabile POST "giorni" è impostata
    if (isset($_POST["giorni"])) {
        // Ottieni i giorni dalla variabile POST
        $giorni = $_POST["giorni"];

        // Se $giorni non è un array, creane uno con un solo elemento
        if (!is_array($giorni)) {
            $giorni = [$giorni];
        }

        // Se la variabile POST "fascia" è impostata
        if (isset($_POST["fascia"])) {
            // Ottieni le fasce orarie dalla variabile POST
            $fascia = $_POST["fascia"];

            // Se $fascia non è un array, creane uno con un solo elemento
            if (!is_array($fascia)) {
                $fascia = [$fascia];
            }

            // Se la variabile POST "nome" è impostata
            if (isset($_POST["nome"])) {
                // Ottieni il nome dalla variabile POST e formattalo con la prima lettera maiuscola
                $nome = ucwords($_POST["nome"]);

                // Se la lunghezza del nome è zero, imposta un messaggio di errore
                if (strlen(trim($nome)) == 0) {
                    $err_msg = "Il nome non è indicato.";
                } else if (preg_match('/\d/', $nome)) {
                    // Se il nome contiene numeri, imposta un messaggio di errore
                    $err_msg = "Il nome non deve contenere numeri.";
                } else {
                    // Altrimenti, salva le informazioni utilizzando la funzione di salvataggio
                    $save($nome, $giorni, $fascia);
                }
            } else {
                // Se la variabile POST "nome" non è impostata, imposta un messaggio di errore
                $err_msg = "Il nome non è stato inserito.";
            }
        } else {
            // Se la variabile POST "fascia" non è impostata, imposta un messaggio di errore
            $err_msg = "Le fascie orarie non sono state inserite.";
        }
    } else {
        // Se la variabile POST "giorni" non è impostata, imposta un messaggio di errore
        $err_msg = "I giorni non sono stati inseriti.";
    }
?>

<!-- Inizia la sezione HTML della pagina -->
<!DOCTYPE html>
<html lang="it">
<head>
    <!-- Impostazioni per il rendering e la visualizzazione della pagina -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Titolo della pagina -->
    <title>Registrazione</title>

    <!-- Collegamento al file CSS di Bootstrap per la formattazione della pagina -->
    <link href="./bootstrap-5.3.2-dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Contenuto principale della pagina -->

    <!-- Div per visualizzare messaggio di errore o conferma -->
    <div class="mt-3 ml-3">
        <div class="row">
            <div class="col h3">
                <?php 
                    // Mostra un messaggio di errore o conferma
                    echo $err_msg == null ? "Disponibilità $nome registrata" : $err_msg; 
                ?>
            </div>
        </div>

        <!-- Pulsanti per nuovi inserimenti e riepilogo -->
        <div class="row">
            <div class="col-auto">
                <a href="index.php" class="btn btn-outline-primary ">Nuovo inserimento</a>
            </div>
            <div class="col-auto">
                <a href="riepilogo.php" class="btn btn-outline-success">Riepilogo</a>
            </div>
        </div>
    </div>

    <!-- Collegamento al file JavaScript di Bootstrap per funzionalità aggiuntive -->
    <script src="./bootstrap-5.3.2-dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
