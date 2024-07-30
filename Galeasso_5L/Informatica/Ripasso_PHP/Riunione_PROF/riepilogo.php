<?php 
    // Avvia una sessione PHP o ripristina quella corrente se esiste
    session_start();
    
    // Verifica se la variabile di sessione disp è impostata
    if(!isset($_SESSION["disp"])){
        // Mostra un messaggio di errore e fornisce un link per tornare alla schermata principale
        echo "<center><a href='index.html'>TORNA ALLA SCHERMATA"
            . " PRINCIPALE e REGISTRA QUALCHE DISPONIBILITA'</a></center>";
    }else{
        // Inizializza un array associativo per tracciare il numero di persone disponibili in ogni giorno e fascia oraria
        $contatori = array(
            "lunedi" => array(
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
            // ... Ripetere lo stesso schema per gli altri giorni della settimana
        );
        
        // Inizializza un array per tenere traccia delle fasce orarie con il massimo numero di disponibilità
        $maxDisp = array();
        // Inizializza una variabile per tenere traccia del massimo numero di disponibilità
        $qtaDisp = 0;
        
        // Itera attraverso le disponibilità memorizzate nella variabile di sessione
        foreach($_SESSION["disp"] as $arr_disp_persona){
            foreach($arr_disp_persona as $giorno => $arr_orari){
                foreach($arr_orari as $orario){
                    // Aumenta il contatore di quel orario in quel giorno
                    $contatori[$giorno][$orario] += 1;
                    $qta = $contatori[$giorno][$orario];
                    
                    // Aggiorna il massimo di disponibilità
                    if($qta == $qtaDisp){
                        $qtaDisp = $qta;
                        $maxDisp[$giorno][$orario] = $qta;
                    }else if($qta > $qtaDisp){
                        $maxDisp = array(); // Resetta l'array se c'è un nuovo massimo
                        $qtaDisp = $qta;
                        $maxDisp[$giorno][$orario] = $qta;
                    }
                }
            }
        }
        
        // Inizializza un array per tenere traccia delle persone mancanti in ciascuna fascia oraria e giorno
        $riepilogoMancanti = array();
        // Itera attraverso le fasce orarie e i giorni con massima disponibilità
        foreach($maxDisp as $giorno => $orari){
            $contatoreMancanti = 0;
            foreach($orari as $orario => $qtaDisp){
                foreach($_SESSION["disp"] as $persona => $disp){
                    // Verifica se la persona non ha disponibilità per questo giorno o questa ora
                    if(!isset($disp[$giorno]) || !in_array($orario, $disp[$giorno])){
                        $riepilogoMancanti[$giorno][$orario][$contatoreMancanti] = $persona;
                    }else{
                        // Segna che non manca nessuno
                        $riepilogoMancanti[$giorno][$orario][$contatoreMancanti] = null;
                    }
                    $contatoreMancanti++;
                } 
            }
        }
?>
<!-- Inizia la sezione HTML della pagina -->
<html>
    <head>
        <!-- Definizione del titolo della pagina -->
        <title>Riepilogo</title>
        
        <!-- Stile CSS inline per la formattazione della tabella e del pulsante di reset -->
        <style>
            .giorni {
                text-align: left;
            }
            td {
                text-align: center;
            }
            #resetButton {
                position: absolute;
                right: 30px;
                width: 80px;
                height: 50px;
            }
        </style>
    </head>
    <body>
        <!-- Sezione per elencare le persone registrate -->
        <div style="position: absolute; top: 0px">
            <h4>Persone registrate:</h4>
            <ul>
                <?php 
                    // Itera attraverso le chiavi dell'array di sessione e stampa ciascuna persona in una lista
                    foreach(array_keys($_SESSION["disp"]) as $persona ){
                        echo "<li>".$persona."</li>";
                    }
                ?>
            </ul>
        </div>
        
        <!-- Sezione centrale della pagina -->
        <center>
            <!-- Pulsante per reset tabella -->
            <button id="resetButton"><a href="resettaSessione.php">Resetta tabella</a></button>
            
            <!-- Tabella per visualizzare il riepilogo delle disponibilità -->
            <table border="1px">
                <!-- Intestazione della tabella -->
                <tr>
                    <td></td>
                    <th>9 - 11</th>
                    <th>11 - 13</th>
                    <th>14 - 16</th>
                    <th>16 - 18</th>
                </tr>
                
                <!-- Righe della tabella per ogni giorno -->
                <tr>
                    <th class="giorni">Lunedi</th>
                    <td><?php echo $contatori["lunedi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["16-18"]; ?></td>
                </tr>
                <!-- Ripetere lo stesso schema per gli altri giorni della settimana -->
                
            </table>
            
            <!-- Intestazione per le fasce con massime disponibilità -->
            <h2>Fasce con massime disponibilita</h2>
            
            <!-- Div per visualizzare le fasce con massime disponibilità -->
            <div style="font-family: cursive">
                <?php 
                    // Itera attraverso le fasce orarie e i giorni con massima disponibilità
                    foreach($riepilogoMancanti as $giorno => $orari){
                        foreach($orari as $orario => $persone){
                            // Mostra il giorno e l'orario
                            echo "<b>$giorno</b> alle <b>$orario</b><br />";
                            $contatoreMancanti = 0;

                            // Itera attraverso le persone e mostra chi manca
                            foreach($persone as $persona){
                                if($persona != null){
                                    echo "Manca $persona\n";
                                    $contatoreMancanti++;
                                }
                            }
                            
                            // Se non manca nessuno, mostra un messaggio
                            if($contatoreMancanti == 0){ 
                                echo "Non manca nessuno.<br />";
                            }else{ 
                                echo "<br /><br />";
                            }
                        }
                    }
                ?>
            </div>
            
            <!-- Link per registrare una nuova disponibilità -->
            <br><br>
            <a href="index.html">REGISTRA UNA NUOVA DISPONIBILITA'</a>
        </center>
    </body>
</html>
<?php 
    // Chiude il blocco else del controllo iniziale
    }
?>
