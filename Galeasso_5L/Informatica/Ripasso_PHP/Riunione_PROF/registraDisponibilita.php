<?php 
    // Controlla se il pulsante "btnInvia" è stato premuto
    if(isset($_POST["btnInvia"])){

        // Controlla se il campo "nome" nel modulo non è vuoto
        if(!empty($_POST["nome"])){
            
            // Inizia o riprende una sessione PHP
            session_start();

            // Stampa le informazioni attuali della sessione (debugging)
            echo "<p><pre>";
            print_r($_SESSION);
            echo "</pre></p>";

            /*
             * $_SESSION["disp"] è un array associativo che contiene le disponibilità delle persone.
             * Esempio:
             * array(
             *     "luca" => array(
             *         [0] => "9-11",
             *         [1] => "14-16"
             *     ),
             *     "giorgio" => ...
             * )
             */

            // Se la persona non è già stata registrata
            if( !isset($_SESSION["disp"][$_POST["nome"]]) ){

                // Se sono stati inseriti almeno un giorno e un orario
                if(isset($_POST["giorni"]) && isset($_POST["orari"])){
                    
                    // Inizializza un array per le disponibilità
                    $disponibilita = array();

                    // Cicla attraverso i giorni selezionati nel modulo
                    foreach($_POST["giorni"] as $giorno){
                        // Crea un array associativo con giorni come chiavi e orari come valori
                        $disponibilita[$giorno] = $_POST["orari"];
                    }

                    // Aggiunge le disponibilità della persona alla sessione
                    $_SESSION["disp"][ $_POST["nome"] ] = $disponibilita;

                    // Stampa un messaggio di conferma
                    echo "Disponibilità di ".$_POST["nome"]." AGGIUNTE.\n";
                }else{
                    // Stampa un messaggio se non sono stati inseriti giorni e orari
                    echo $_POST["nome"]." NON SEI REGISTRATO,\nSE VUOI ESSERE"
                            . " REGISTRATO INSERISCI ALMENO\nUN GIORNO E UN ORARIO !\n\n";
                    // Distrugge la sessione
                    session_destroy();
                }
            }else{  // La persona è già stata registrata
                $disponibilita = $_SESSION["disp"][$_POST["nome"]];
                
                // Se sono stati inseriti il nome ma nessun giorno o orario, cancella la persona
                if(!isset($_POST["giorni"]) && !isset($_POST["orari"])){
                    unset($_SESSION["disp"][ $_POST["nome"] ]);
                    echo $_POST["nome"]." È STATO CANCELLATO.\n";
                }else{
                    // Se sono stati inseriti i giorni
                    if(isset($_POST["giorni"])){
                        foreach($_POST["giorni"] as $giorno){
                            // Se quel giorno non è settato, lo aggiunge 
                            if( !isset($disponibilita[$giorno]) ){
                                $disponibilita[$giorno] = $_POST["orari"];

                                echo "Aggiunte disponibilità di ".$_POST["nome"]." per $giorno.\n";
                            }else{
                                // Se ha inserito degli orari, sovrascrive gli orari precedenti
                                if(!isset($_POST["orari"])){
                                    unset($disponibilita[$giorno]);
                                    echo "Eliminata la/e DISPONIBILITA' di ".$_POST["nome"]. " per $giorno\n";
                                }else{  // Orari non settati ==> cancella quel giorno
                                    if($disponibilita[$giorno] != $_POST["orari"]){
                                        $disponibilita[$giorno] = $_POST["orari"];
                                        echo "Disponibilità di ".$_POST["nome"]." AGGIORNATE". " per $giorno\n";
                                    }else{
                                        echo "Disponibilità di ".$_POST["nome"]." LASCIATE UGUALI". " per $giorno\n";
                                    }
                                }
                            }
                        }
                        
                        // Se ha eliminato le disponibilità di un giorno e non ne ha rimasti, cancella la persona
                        if(count($disponibilita) > 0){
                            $_SESSION["disp"][ $_POST["nome"] ] = $disponibilita;
                        }else{
                            unset($_SESSION["disp"][ $_POST["nome"] ]);
                            echo $_POST["nome"]." È STATO CANCELLATO.\n";
                        }
                    }else{
                        // Stampa un messaggio se mancano i giorni
                        echo "Ehi dovresti inserire PERLOMENO i giorni !!!\n"
                        . "(a meno che tu non voglia cancellare la persona)\n";
                    }
                }
            }
        }else{
            // Stampa un messaggio se mancano i dati
            echo "DEVI INSERIRE I DATI !!!\n";
        }
    }else{
        // Stampa un messaggio se l'utente è arrivato in modo imprevisto al codice
        echo "Come sei arrivato qui !?\n";
    }
?>
<!-- Link per tornare alla pagina iniziale -->
<a href='index.html'>CLICCA PER TORNARE ALLA PAGINA INIZIALE</a><br>

<?php 
    // Se ha cancellato un nome dalla lista e la lista è vuota, non deve avere la possibilità di andare nel RIEPILOGO
    if(isset($_SESSION["disp"])){
        $qtaDisp = count($_SESSION["disp"]);
        
        // Se la lista è vuota, distrugge la sessione
        if($qtaDisp == 0){ 
            session_destroy();
        }else{
            // Link per andare al riepilogo
            ?>
<a href='riepilogo.php'>CLICCA PER ANDARE AL RIEPILOGO</a>
<?php 
        }
    }
?>
</pre></center>
