<html>
	<body>
		<h2>Esempio cookies e sessioni</h2>
		<form action="index.php" method="post">
			Utente: <input type="text" name="nomeUt"><br>
			Password: <input type="text" name="pswUt"><br>
			Colore preferito: <input type="text" name="colore"><br>
			 <input type="submit" name="send" value="Login">
		</form>
		
		<?php

           // Definizione di un array associativo $Utenti contenente informazioni su utenti e password
           $Utenti = array(
                "Utente1" => array (
                    "Password" => 123,
                    "Colore" => "rosso"
                ),
                "Utente2" => array (
                    "Password" => 456,
                    "Colore" => "blu"
                ),
                "Utente3" => array (
                    "Password" => 789,
                    "Colore" => "verde"
                )
           );
				
            // Debug: Mostra la struttura dell'array $Utenti
            echo "<pre>";
            //print_r($Utenti);
            echo "</pre>";

            // Recupero dei valori inviati tramite il form tramite il metodo POST
            $nome = $_POST['nomeUt'];
            $pasw = $_POST['pswUt'];
            $colore = $_POST['colore'];

            // Controllo se è stato inviato un nome utente
            if (!empty($_POST['nomeUt'])) {
                // Controllo se il nome utente esiste nell'array $Utenti
                if (array_key_exists($nome, $Utenti)) {
                    // Controllo se è stata inviata una password
                    if (!empty($_POST['pswUt'])) {
                        // Controllo se la password inserita corrisponde a quella nell'array $Utenti
                        if ($Utenti[$nome]['Password'] == $pasw) {
                            echo "Password corretta!<br>";

                            // Controllo se è stata inviata la preferenza del colore
                            if (!empty($_POST['colore'])) {
                                // Controllo se il colore inserito corrisponde a quello nell'array $Utenti
                                if ($Utenti[$nome]['Colore'] == $colore) {
                                    echo "Il colore è corretto!!<br>";
                                    
                                    // Impostazione dei cookies
                                    setcookie("nomeu", $nome, time()+3600);
                                    setcookie("pswdu", $pasw, time()+3600);
                                    setcookie("coloru", $colore, time()+3600);
                                    
                                    // Inizializzazione delle variabili di sessione
                                    session_start();
                                    $_SESSION['Snomeu'] = $nome;
                                    $_SESSION['Spswdu'] = $pasw;
                                    $_SESSION['Scoloru'] = $colore;
                                    
                                    // Redirezionamento alla pagina "benvenuto.php"
                                    header("Location: benvenuto.php");
                                } else {
                                    echo "Il colore è sbagliato!<br>";
                                }                        
                            } else {
                                echo "Non hai indicato il colore!<br>";
                            }
                        } else {
                            echo "Password errata!<br>";
                        }
                    } else {
                        echo "Non hai indicato la password!<br>";
                    }
                } else {
                    echo "Nome utente non trovato!<br>";
                }
            } else {
                echo "Non hai indicato il nome utente<br>";
            }
        ?>
	</body>
</html>
