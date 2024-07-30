<?php
	if(!isset($_COOKIE["username"])){
		header("Location: ./destroyer.php");
      exit;
	} else {
		 if((intval($_COOKIE['testCookie']) - time()) < 1){
			  echo "Il cookie scade ora!<br>";
		 }else{
			  echo "<a href='protected.php'>Aggiornare</a> la pagina per calcolare quanto manca alla scadenza della sessione!<br><br>";
			  echo "<br>Il cookie scade tra " . (intval($_COOKIE['testCookie']) - time()) . " secondi<br>";
		 }	
	}
   session_start();

//parametri connessione al DBMS MariaDB
	$host = "localhost";
	$user = "root";
	$password = "";
	$dbname = "GaleassoPreparazioneVerificaPHP";

    if(!isset($_SESSION["username"])){
        header("Location: ./login.php");
        exit;
    }

//connessione al DBMS con scelta immediata del DB da usare
    $conn = new mysqli($host, $user, $password, $dbname);
    if($conn->connect_error){
        die("Connessione ad DB fallita! ".$conn->connect_error);
    }

//query preparata
    $query = "SELECT * FROM Utenti WHERE username=?";
    $stmt = $conn->prepare($query);
    if(!$stmt){
        die("Preparazione della query fallita: ".$conn->error);
    }
    $stmt->bind_param("s", $_SESSION["username"]);

//eseguiamo la query
	$stmt->execute();

//otteniamo il risulatato della query
    $result = $stmt->get_result();

    if($result->num_rows==0){
        //lo username passato non esiste nel db
        //distruggiamo la sessione e riportiamo l'utente al login
        session_destroy();
        header("Location: ./login.php");
        exit;
    }

	include './DB.php';
	Database::collegati();

	$tabella_utenti = 'SELECT * FROM Utenti;';
    $tabella_post = 'SELECT * FROM posts;';

    $dati_user = Database::executeQuery($tabella_utenti)->fetch_all(MYSQLI_ASSOC);
    $dati_post = Database::executeQuery($tabella_post)->fetch_all(MYSQLI_ASSOC);
?>
<html lang="en">
<head>
	<title>Sessione autenticata</title>
</head>
<body>
	<form action="" method="post">
		<div>
			<br><input type="submit" name="rilancia" value="Tieni viva la sessione..."/>
		</div>
	</form>
</body>
</html>

<?php
    echo "<h1>Sessione autenticata...</h1>";
    echo "<a href='./destroyer.php'> Destroyer </a>";
    
    if(isset($_POST["rilancia"])){
		$time = time()+120;
		$timeMemo = (string)$time;
		//sets cookie with expiration time defined above
		setcookie("testCookie", "".$timeMemo."", $time+10);
		setcookie("username", $_SESSION["username"], $time);
	}
?>

<html lang="en">
<head>
	<title>Sessione autenticata</title>
</head>
<body>
<hr/>
    <div>
        <div>
            <h2>Benvenuto nella home</h2>
        </div>

		<div>
            <form class="form" action="./addPost.php" method="POST">
				</br>
                <span><strong>Inserisci Post</strong></span>
                <div>
                    <input type="text" name="id_utente" placeholder="ID Utente">
                    <input type="text" name="titolo_post" placeholder="Titolo">
                    <input type="text" name="contenuto_post" placeholder="Contenuto">
                </div>
                <input type="submit" value="Aggiungi">
            </form>
        </div>

		<div>
		<div>
            <h2>Benvenuto nella home</h2>
        </div>           
		<?php
			for($i=0; $i < count($dati_user); $i++){
				echo $dati_user[$i]['username']." ";
			}
		?>
		</div>
		</br>
		<div>
			<?php
				for($i=0; $i < count($dati_post); $i++){
					echo $dati_post[$i]['username']." ";
					echo $dati_post[$i]['title']." ";
					echo $dati_post[$i]['content']."</br>";
				}
			?>
		</div>
		</div>
</body>
</html>