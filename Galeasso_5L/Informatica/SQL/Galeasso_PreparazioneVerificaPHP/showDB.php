<?php
    include './DB.php';

    Database::collegati();

    $tabella_utenti = 'SELECT * FROM Utenti;';
    $tabella_post = 'SELECT * FROM posts;';

    $dati_user = Database::executeQuery($tabella_utenti)->fetch_all(MYSQLI_ASSOC);
    $dati_post = Database::executeQuery($tabella_post)->fetch_all(MYSQLI_ASSOC);
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Visualizza DB</title>
</head>
<body>
    <div>
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
</body>
</html>