<?php
    include './database.php';
    session_start();
    Database::connessione();

    if (isset($_COOKIE['idRelatore'])) {
        $idRelatore = $_COOKIE['idRelatore'];

		$queryRelatore = "SELECT NomeRel, CognomeRel FROM RELATORE WHERE IDRel = $idRelatore";
		$risultatoRelatore = Database::eseguiQuery($queryRelatore);
		$relatore = $risultatoRelatore->fetch_assoc();
		$nomeRelatore = $relatore['NomeRel'];
		$cognomeRelatore = $relatore['CognomeRel'];

        $querySpeechRelatore = "
            SELECT 
                Speech.Titolo, Speech.Argomento, Programma.FasciaOraria, Programma.NomeSala,
                Sala.NpostiSala, Sala.Numero,
                RELATORE.NomeRel, RELATORE.CognomeRel
            FROM 
                Speech, Programma, Sala, RELAZIONA, RELATORE
            WHERE 
                Speech.IDSpeech = Programma.IDSpeech
                AND Programma.NomeSala = Sala.NomeSala
                AND Programma.IDProgramma = RELAZIONA.IDProgramma
                AND RELAZIONA.IDRel = RELATORE.IDRel
                AND RELATORE.IDRel = $idRelatore
        ";

        $risultato = Database::eseguiQuery($querySpeechRelatore);
        $card = $risultato->fetch_all(MYSQLI_ASSOC);
    } else {
        echo "ID del relatore non trovato nel cookie.";
    }
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galeasso Convention - Relatore</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/styleRelatore.css">
	<style>
		.card-title {
			color: #007BFF;
		}
	</style>
</head>
<body class="pattern">
    <div class="container mt-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
			<h1>Portale Relatore - <?php echo $nomeRelatore . ' ' . $cognomeRelatore; ?></h1>
            <a href="../php/logout.php" class="btn btn-danger">Logout</a>
        </div>
        <div class="login-container">
            <?php if (count($card) === 0): ?>
                <p class="p-warning">Nessuno speech disponibile per questo relatore.</p>
            <?php else: ?>
                <?php foreach ($card as $row): ?>
                    <div class="card bg-dark text-white mb-3">
                        <div class="card-body">
                            <h4 class="card-title"><?php echo $row['Titolo']; ?></h4>
                            <p class="card-text"><strong>Relatore:</strong> <?php echo $row['NomeRel'] . ' ' . $row['CognomeRel']; ?></p>
                            <p class="card-text"><strong>Argomento:</strong> <?php echo $row['Argomento']; ?></p>
                            <p class="card-text"><strong>Fascia oraria:</strong> <?php echo $row['FasciaOraria']; ?></p>
                            <p class="card-text"><strong>Nome della sala:</strong> <?php echo $row['NomeSala']; ?></p>
                            <p class="card-text"><strong>Posti disponibili:</strong> <?php echo $row['NpostiSala']; ?></p>
                            <p class="card-text"><strong>Piano:</strong> <?php echo $row['Numero']; ?></p>
                        </div>
                    </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
