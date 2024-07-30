<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Galeasso Riunioni</title>
</head>
<body>
	<h1>Esercizio Riunioni</h1><br/>
	<form action="dati.php" method="post">
		Nome: <input type="text" name="nome" id="nome" placeholder="Inserisci il nome della persona" required><br/><br/>

		<select name="giorni">
			<option value="Lunedì">Lunedì</option>
			<option value="Martedì">Martedì</option>
			<option value="Mercoledì">Mercoledì</option>
			<option value="Giovedì">Giovedì</option>
			<option value="Venerdì">Venerdì</option>
			<option value="Sabato">Sabato</option>
			<option value="Domenica">Domenica</option>
		</select>

		<select name="orari">
			<option value="9-11">9-11</option>
			<option value="11-13">11-13</option>
			<option value="14-16">14-16</option>
			<option value="16-18">16-18</option>
		</select><br/><br/>

		<input type="submit" value="Invia">
	</form>
</body>
</html>