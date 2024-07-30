<?php
    // Richiedi il file data.php che potrebbe contenere dati utilizzati nel codice
    require "./data.php";

    // Includi il file enable_debug.php che potrebbe contenere configurazioni per il debug
    include "./enable_debug.php";

    // Inizia o ripristina una sessione PHP
    session_start();
    
    // Se la variabile di sessione "day" non è impostata
    if(!isset($_SESSION["day"])){
        // Mostra un messaggio di avviso e reindirizza alla pagina di reset della sessione dopo 1 secondo
        echo '<script type="text/javascript">alert("Non è ancora presente alcuna prenotazione valida!");</script>';
        header("Refresh:1; url='resetSess.php'");
        exit();
    }

    // Debug: Stampa la variabile di sessione e interrompi l'esecuzione
    echo "<p><pre>";
    print_r($_SESSION);
    echo "</pre></p>";

    // Inizializza un array associativo per il conteggio massimo di partecipanti e le fasce orarie con quel massimo
    $mc = [
        "num" => 0,
        "fgp" => [],
    ];

    // Inizializza un array per contenere tutti i nomi registrati
    $all_name = [];

    // Itera attraverso i giorni e le fasce orarie
    foreach($day_map as $day){
        foreach($h_map as $h){
            // Conta il numero di partecipanti in una determinata fascia oraria
            $c = count($_SESSION["day"][$day][$h]);
            
            // Aggiorna il massimo numero di partecipanti
            if($c > $mc["num"]){
                $mc["num"] = $c;
                $mc["fgp"] = [];
            }

            // Se il numero di partecipanti è uguale al massimo, aggiungi la fascia oraria all'array
            if($c === $mc["num"]){
                $mc["fgp"][] = [
                    $day, 
                    $h,
                    []
                ];
            }

            // Unisci i nomi registrati in tutte le fasce orarie
            $all_name = array_merge($all_name, $_SESSION["day"][$day][$h]);
        }
    }

    // Debug: Stampa la lista di tutti i nomi e il conteggio massimo
    echo "<p><pre>";
    print_r($all_name);
    print_r($mc);
    echo "</pre></p>";

    // Rimuovi duplicati dalla lista di tutti i nomi
    $all_name = array_unique($all_name);

    // Itera attraverso le fasce orarie con il massimo numero di partecipanti
    foreach($mc["fgp"] as list($day, $h, &$diff)){
        // Ottieni i nomi registrati per quella fascia oraria
        $names = $_SESSION["day"][$day][$h];

        // Trova le differenze tra la lista completa dei nomi e i nomi registrati
        $diff = array_diff($all_name, $names);

        // Debug: Stampa la lista delle differenze
        echo "<p><pre>";
        print_r($diff);
        echo "</pre></p>";
    }

    // Debug: Stampa nuovamente il conteggio massimo e le fasce orarie con massimo numero di partecipanti
    echo "<p><pre>";
    print_r($mc);
    echo "</pre></p>";
?>
<!-- Inizia la sezione HTML della pagina -->
<!DOCTYPE html>
<html lang="it">
<head>
    <!-- Impostazioni per il rendering e la visualizzazione della pagina -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Titolo della pagina -->
    <title>Prenotazione riunione</title>

    <!-- Collegamento al file CSS di Bootstrap per la formattazione della pagina -->
    <link href="./bootstrap-5.3.2-dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Contenuto principale della pagina -->

    <!-- Contenitore principale della pagina -->
    <div class="container">
        <!-- Titolo della tabella delle disponibilità registrate -->
        <div class="row">
            <div class="col h2">
                Tabella delle disponibiltà registrate
            </div>
        </div>
        
        <!-- Tabella per visualizzare le disponibilità registrate -->
        <table class="table">
            <thead>
                <tr>
                    <th scope="col"></th>
                    <?php
                        // Itera attraverso i giorni e aggiungi l'intestazione della tabella
                        foreach($day_map as $day){
                    ?>
                        <th scope="col"><?=$day?></th>
                    <?php 
                        }
                    ?>
                </tr>
            </thead>
            <tbody>
                <?php
                    // Itera attraverso le fasce orarie e aggiungi le righe della tabella
                    foreach($h_map as $h){
                ?>
                    <tr>
                        <th><?=$h?></th>
                        <?php 
                            // Itera attraverso i giorni e aggiungi il numero di partecipanti per ogni fascia oraria
                            foreach($day_map as $day){
                        ?>
                            <td><?=count($_SESSION["day"][$day][$h])?></td>
                        <?php
                            }
                        ?>
                    </tr>
                <?php 
                    }
                ?>
            </tbody>
        </table>

        <!-- Titolo delle fasce con massima disponibilità -->
        <div class="row">
            <div class="col h2">
                Fasce con massima disponibilità
            </div>
        </div>

        <!-- Sezione per visualizzare le fasce con massima disponibilità -->
        <div>
            <?php
                // Itera attraverso le fasce con massimo numero di partecipanti
                foreach($mc["fgp"] as list($day, $h, &$diff)){
            ?>
                <div class="row mt-3">
                    <div class="col">
                        <?="$day - $h"?>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <?=count($diff) == 0 ? "Tutti partecipano" : "Non disponibile: ".join(", ", $diff)?>
                    </div>
                </div>
            <?php 
                }
            ?>
        </div>

        <!-- Pulsanti per nuovi inserimenti e reset della tabella -->
        <div class="row mt-3">
            <div class="col-auto"><a href="index.php" class="btn btn-outline-primary ">Nuovo inserimento</a></div>
            <div class="col-auto"><a href="resetSess.php" class="btn btn-outline-primary ">Resetta tabella</a></div>
            <p></p>
        </div>
    </div>

    <!-- Collegamento al file JavaScript di Bootstrap per funzionalità aggiuntive -->
    <script src="./bootstrap-5.3.2-dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
