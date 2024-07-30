<?php
	session_start();
	session_destroy();

//parametri connessione al DBMS MariaDB
	$host = "localhost";
	$user = "root";
	$password = "";
	$dbname = "GaleassoPreparazioneVerificaPHP";

	$last_login = "18-04-2024";
	$last_login_converted = date("Y-m-d", strtotime($last_login));

//connessione al DBMS con scelta immediata del DB da usare
	$conn = new mysqli($host, $user, $password, $dbname);
	if($conn->connect_error){
		die("Connessione ad DB fallita! ".$conn->connect_error);
	}

//leggo parametri form
	if(isset($_POST["submit"])){
		$username = $_POST["username"];
		$password = hash("sha256", $_POST["password"]);
//query preparata
		$query = "SELECT * FROM Utenti WHERE username=? AND password=? AND last_login=?";
		$stmt = $conn->prepare($query);
		$stmt->bind_param("sss", $username, $password, $last_login_converted);
		//echo "nome: $username - paswd: $password - data: ".strtotime($last_login)."<br>";

//eseguiamo la query
		$stmt->execute();

//otteniamo il risulatato della query
		$result = $stmt->get_result();
		
//controllo numero righe
		if($result->num_rows>0){
			session_start();
			$_SESSION["logged_in"]=true;
			$_SESSION["username"]=$username;
			
			$time = time()+120;
			$timeMemo = (string)$time;
			//sets cookie with expiration time defined above
			setcookie("testCookie", "".$timeMemo."", $time+10);
			setcookie("username", $username, $time);
			header("Location: ./protected.php");
		}else{
			echo "user e pass non trovati o non autorizzati!";
		}
	}

?>

<html lang="en">
<head>
	<title>Esempi Web</title>
</head>
<body>
	<div id="container">
		<div id="cont">
			<h1>Esercizio PHP - SQL</h1>
			<form action="" method="post">
				<div>
					<input class="inptx" type="text" name="username" placeholder="Inserire nome"/>
				</div>
				<div>
					<input class="inptx" type="password" name="password" placeholder="Inserire password"/>
				</div>
				<div>
					<input class="btn" type="submit" name="submit" value="Login"/>
				</div>
			</form>
		</div>

		<div>
            <form action="./createTB.php" method="POST">
                <input type="submit" value="Crea tabelle">
            </form>
			<form action="./deleteTB.php" method="POST">
                <input type="submit" value="Elimina tabelle">
            </form>
        </div>
	</div>
</body>
</html>
