<?php
    include './DB.php';

    Database::collegati();

    $tabella_user = 'SELECT * FROM users;';
    $tabella_post = 'SELECT * FROM posts;';

    $dati_user = Database::executeQuery($tabella_user)->fetch_all(MYSQLI_ASSOC);
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
	<a href="./index.html">Home</a>
        <a href="./addPost.html">Aggiungi post</a>
        <a href="./addUser.html">Aggiungi utente</a>
        <a href="./showDB.php">Visualizza DB</a>
    </div>

    <div>
		<?php
			for($i=0; $i < count($dati_user); $i++){
				echo "<br>". $dati_user[$i]['user_id']." ";
				echo $dati_user[$i]['username']." ";
				echo $dati_user[$i]['email'];
			}
		?>
    </div>
	</br>
    <div>
		<?php
			for($i=0; $i < count($dati_post); $i++){
				echo $dati_post[$i]['user_id']." ";
				echo $dati_post[$i]['user_id']." ";
				echo $dati_post[$i]['title']." ";
				echo $dati_post[$i]['content']."</br>";
			}
		?>
	</div>
</body>
</html>