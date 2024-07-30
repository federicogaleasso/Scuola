<?php
	include './database.php';
	session_start();
	Database::connessione();

	$querySpeechDisponibili = "SELECT Titolo, Argomento, Sala.NomeSala, FasciaOraria, NpostiSala, Numero, NomeRel, CognomeRel, Programma.IDProgramma, Speech.IDSpeech FROM Speech, Programma, Sala, RELAZIONA, RELATORE WHERE Speech.IDSpeech = Programma.IDSpeech AND Programma.NomeSala = Sala.NomeSala AND Programma.IDProgramma = RELAZIONA.IDProgramma AND RELAZIONA.IDRel = RELATORE.IDRel";
	$risultato = Database::eseguiQuery($querySpeechDisponibili);
	$speechDisponibili = $risultato->fetch_all(MYSQLI_ASSOC);
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portale Admin</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/stylePortaleAdmin.css">
	<style>
		.card-title {
			color: #007BFF;
		}
	</style>
</head>
<body class="pattern">
    <div class="container mt-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1>Portale Admin</h1>
            <a href="../php/logout.php" class="btn btn-danger">Logout</a>
        </div>
        <div class="login-container">
            <h2 class="text-center">Registrazione Relatore</h2>
            <form action='../php/registrazioneRelatore.php' method='post'>
                <p class="font-weight-bold">Dati del relatore</p>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder='Inserisci il nome' name='nome' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder='Inserisci il cognome' name='cognome' required/>
                </div>
                <div class="form-group">
                    <input type='email' class="form-control" placeholder='Inserisci la mail' name='email' required/>
                </div>
                <div class="form-group">
                    <input type='password' class="form-control" placeholder='Inserisci la password' name='password' required/>
                </div>
                <p class="font-weight-bold mt-4">Dati dell'azienda</p>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci la ragione sociale dell'azienda" name='ragioneSocialeAzienda' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci l'indirizzo dell'azienda" name='indirizzoAzienda' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci il numero di telefono" name='telefonoAzienda' required/>
                </div>
                <p class="font-weight-bold mt-4">Dati dello speech</p>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci il titolo dello speech" name='titolo' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci l'argomento dello speech" name='argomento' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci la fascia oraria" name='fasciaOraria' required/>
                </div>
                <div class="form-group">
                    <input type='text' class="form-control" placeholder="Inserisci il nome della sala" name='nomeSala' required/>
                </div>
                <div class="form-group">
                    <input type='number' class="form-control" placeholder="Inserisci il numero di posti della sala" name='nPostiSala' required/>
                </div>
                <div class="form-group">
                    <input type='number' class="form-control" placeholder="Inserisci il piano" name='numero' required/>
                </div>
                <button type='submit' class="btn btn-primary btn-block mt-4">Registra Relatore</button>
            </form>
        </div>
        <div class="login-container mt-5 mb-5">
            <h2 class="text-center">Cancella Speech</h2>
            <div class="row mt-4">
				<?php if (empty($speechDisponibili)): ?>
						<p class="p-warning">Nessuno speech disponibile.</p>
				<?php else: ?>
					<?php foreach ($speechDisponibili as $row): ?>
						<div class="col-md-3 mb-4">
							<div class="card bg-dark text-white">
								<div class="card-body">
									<h4 class="card-title"><?php echo $row['Titolo']; ?></h4>
									<p class="card-text"><strong>Relatore:</strong> <?php echo $row['NomeRel'] . ' ' . $row['CognomeRel']; ?></p>
									<p class="card-text"><strong>Argomento:</strong> <?php echo $row['Argomento']; ?></p>
									<p class="card-text"><strong>Fascia oraria:</strong> <?php echo $row['FasciaOraria']; ?></p>
									<p class="card-text"><strong>Nome della sala:</strong> <?php echo $row['NomeSala']; ?></p>
									<p class="card-text"><strong>Posti disponibili:</strong> <?php echo $row['NpostiSala']; ?></p>
									<p class="card-text"><strong>Piano:</strong> <?php echo $row['Numero']; ?></p>
									<form method="post" action="./eliminaSpeech.php" class="mt-3">
										<input type="hidden" name="idProgramma" value="<?php echo $row['IDProgramma']; ?>">
										<input type="hidden" name="idSpeech" value="<?php echo $row['IDSpeech']; ?>">
										<input type="hidden" name="nomeSala" value="<?php echo $row['NomeSala']; ?>">
										<button type="submit" class="btn btn-danger">Cancella speech</button>
									</form>
								</div>
							</div>
						</div>
					<?php endforeach; ?>
				<?php endif; ?>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
