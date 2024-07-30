<?php
    // Includi il file enable_debug.php che potrebbe contenere configurazioni per il debug
    include "./enable_debug.php";

    // Definisci una costante per la dimensione di ciascun record
    $SIZE_OF_RECORD = 4;

    // Definisci un array di materie
    $subjects = [
        "Matematica",
        "Inglese",
        "Informatica",
        "TPSIT",
        "Sistemi e Reti"
    ];

    // Verifica la presenza e la completezza dei dati inviati tramite POST
    if (
        !isset($_POST["data"]) || 
        empty($_POST["data"]) ||
        !isset($_POST["firstname"]) ||
        empty($_POST["firstname"]) ||
        !isset($_POST["subject"]) ||
        empty($_POST["subject"])
    ) {
        // Stampa i dati POST (debug)
        var_dump($_POST);

        // Reindirizza alla pagina di indice (index.html)
        header("Location: index.html");
        exit;
    }

    // Decodifica la stringa JSON contenente i dati inviati tramite POST
    $data = json_decode($_POST["data"]);
    $firstname = ucfirst($_POST["firstname"]);
    $subject = ucfirst($_POST["subject"]);

    // Gestione degli errori nella decodifica JSON
    if (JSON_ERROR_NONE != 0) {
        echo "err@Errore nei dati inviati";
        $json_error = json_last_error_msg();
        exit;
    } elseif (!preg_match("/^[a-zA-Z-' ]*$/", $firstname)) {
        echo "err@" . "Il cognome da cercare deve avere solo lettere, apostrofo o spazio";
    } elseif (!in_array($subject, $subjects)) {
        echo "err@" . "Materia da cercare non riconosciuta -> $subject";
        exit;
    }

    // Definisci le chiavi consentite per ogni record
    $keys = ["firstname", "score", "subject", "id"];
    $errorRecord = [];

    // Itera attraverso i dati ricevuti
    foreach ($data as $record) {
        // Verifica se il record è un oggetto e ha la dimensione corretta
        if (!is_object($record)) {
            echo "err@Errore nei dati trasmessi";
            exit;
        } elseif (count((array) $record) != $SIZE_OF_RECORD) {
            echo "err@Errore nei dati trasmessi";
            exit;
        }

        // Itera attraverso le chiavi e i valori del record
        foreach ($record as $key => $value) {
            if (!in_array($key, $keys)) {
                $errorRecord[] = $record->id . "@" . "La chiave $key non è riconosciuto";
                continue 2;
            } elseif ($key == "firstname") {
                // Verifica il formato del nome
                if (!preg_match("/^[a-zA-Z-' ]*$/", $value)) {
                    $errorRecord[] =  $record->id . "@" . "Il nome deve avere solo lettere, apostrofo o spazio";
                    continue 2;
                }
            } elseif ($key == "subject") {
                // Verifica se la materia è riconosciuta
                if (!in_array($value, $subjects)) {
                    $errorRecord[] =  $record->id . "@" . "Materia non riconosciuto";
                    continue 2;
                }
            } elseif ($key == "score") {
                // Verifica se il voto è un intero compreso tra 0 e 10
                if (!gettype($value) == "integer") {
                    $errorRecord[] =  $record->id . "@" . "Il voto deve essere un intero";
                    continue 2;
                } elseif ($value < 0 || $value > 10) {
                    $errorRecord[] =  $record->id . "@" . "Il voto deve essere compreso tra 0 e 10";
                    continue 2;
                }
            }
        }
    }

    // Se non ci sono errori nei record, filtra i record target
    if (count($errorRecord) == 0) {
        $target_records = array_filter($data, function ($val, $key) use ($firstname, $subject) {
            return $firstname === ucfirst($val->firstname) && $subject === ucfirst($val->subject);
        }, ARRAY_FILTER_USE_BOTH);
    } else {
        // Stampa gli errori nei record
        echo implode("\n", $errorRecord);
        exit;
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
    <title><?="Voti di ".$firstname."(".$subject.")"?></title>

    <!-- Stile CSS per la formattazione della tabella -->
    <style>
        th, tr, td{
            border: 1px black solid;
            width: 150px;
        }

        table{
            border: 1px black solid;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
    <?php
        // Se non ci sono record target, mostra un messaggio
        if (count($target_records) == 0) {
    ?>
        <h1><?=$firstname." non ha ancora voto di ".$subject?></h1>
    <?php
        } else {
    ?>
        <!-- Titolo e tabella dei voti -->
        <h1><?="Voto di ".$subject." di ".$firstname?></h1>
        <table>
            <tr>
                <th>Cognome</th>
                <th>Voto</th>
            </tr>
            <?php
                // Itera attraverso i record target e crea le righe della tabella
                foreach ($target_records as $record) {
            ?>
            <tr>
                <td><?=ucfirst($record->firstname)?></td>
                <td><?=$record->score?></td>
            </tr>
    <?php
            }
        }
    ?>
        </table>
</body>
</html>
