<?php
	include './database.php';
	session_start();
	Database::connessione();

	$querySpeechDisponibili = "SELECT Titolo, Argomento, Sala.NomeSala, FasciaOraria, NpostiSala, Numero, NomeRel, CognomeRel, Programma.IDProgramma FROM Speech, Programma, Sala, RELAZIONA, RELATORE WHERE Speech.IDSpeech = Programma.IDSpeech AND Programma.NomeSala = Sala.NomeSala AND Programma.IDProgramma = RELAZIONA.IDProgramma AND RELAZIONA.IDRel = RELATORE.IDRel";
	$risultato = Database::eseguiQuery($querySpeechDisponibili);
	$speechDisponibili = $risultato->fetch_all(MYSQLI_ASSOC);

	if (isset($_COOKIE['idPartecipante'])) {
		$idPartecipante = $_COOKIE['idPartecipante'];

		$queryPartecipante = "SELECT NomePart, CognomePart FROM PARTECIPANTE WHERE IDPart = $idPartecipante";
		$risultatoPartecipante = Database::eseguiQuery($queryPartecipante);
		$partecipante = $risultatoPartecipante->fetch_assoc();
		$nomePartecipante = $partecipante['NomePart'];
		$cognomePartecipante = $partecipante['CognomePart'];

		$querySpeechIscritto = "
			SELECT PROGRAMMA.IDProgramma, Speech.Titolo, Speech.Argomento, PROGRAMMA.FasciaOraria, Sala.NomeSala, Sala.NpostiSala, Sala.Numero, RELATORE.NomeRel, RELATORE.CognomeRel
			FROM PROGRAMMA, SCEGLIE, Speech, Sala, RELAZIONA, RELATORE
			WHERE PROGRAMMA.IDProgramma = SCEGLIE.IDProgramma
			AND PROGRAMMA.IDSpeech = Speech.IDSpeech
			AND PROGRAMMA.NomeSala = Sala.NomeSala
			AND PROGRAMMA.IDProgramma = RELAZIONA.IDProgramma
			AND RELAZIONA.IDRel = RELATORE.IDRel
			AND SCEGLIE.IDPart = $idPartecipante
		";
		$risultato = Database::eseguiQuery($querySpeechIscritto);
		$speechIscritto = $risultato->fetch_all(MYSQLI_ASSOC);
	} else {
		echo "ID del partecipante non trovato nel cookie.";
	}
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galeasso Convention - Partecipante</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/stylePartecipante.css">
	<style>
		.card-title {
			color: #007BFF;
		}
	</style>
</head>
<body class="pattern">
    <div class="container mt-5 mb-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
			<h1>Portale Partecipante - <?php echo $nomePartecipante . ' ' . $cognomePartecipante; ?></h1>
            <a href="../php/logout.php" class="btn btn-danger">Logout</a>
        </div>
        <div class="login-container">
            <?php if (count($speechDisponibili) == 0): ?>
                <p class="p-warning">Nessuno speech disponibile.</p>
            <?php else: ?>
                <div class="row">
                    <?php foreach ($speechDisponibili as $row): ?>
                        <?php 
                            $checkIscritto = false;
                            foreach ($speechIscritto as $speech) {
                                if ($row['IDProgramma'] == $speech['IDProgramma']) {
                                    $checkIscritto = true;
                                    break;
                                }
                            }
                        ?>
                        <div class="col-md-3 mb-4">
                            <div class="card bg-dark text-white">
                                <div class="card-body">
                                    <h4 class="card-title"><strong><?php echo $row['Titolo']; ?></strong></h4>
                                    <p class="card-text"><strong>Relatore:</strong> <?php echo $row['NomeRel'] . ' ' . $row['CognomeRel']; ?></p>
                                    <p class="card-text"><strong>Argomento:</strong> <?php echo $row['Argomento']; ?></p>
                                    <p class="card-text"><strong>Fascia oraria:</strong> <?php echo $row['FasciaOraria']; ?></p>
                                    <p class="card-text"><strong>Nome della sala:</strong> <?php echo $row['NomeSala']; ?></p>
                                    <p class="card-text"><strong>Posti disponibili:</strong> <?php echo $row['NpostiSala']; ?></p>
                                    <p class="card-text"><strong>Piano:</strong> <?php echo $row['Numero']; ?></p>
                                    <form method="post" action="<?php echo $checkIscritto ? './cancellaIscrizioneSpeech.php' : './iscrizioneSpeech.php'; ?>" class="mt-3">
                                        <input type="hidden" name="idProgramma" value="<?php echo $row['IDProgramma']; ?>">
                                        <button type="submit" class="btn <?php echo $checkIscritto ? 'btn-warning' : 'btn-primary'; ?>">
                                            <?php echo $checkIscritto ? 'Cancella iscrizione' : 'Iscriviti'; ?>
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>
        </div>

		<div class="login-container mt-5">
			<div class="table-responsive mt-3">
				<table class="table table-bordered">
					<thead>
						<tr>
							<th>Ora / Sala</th>
							<?php foreach ($speechDisponibili as $row): ?>
								<th><?php echo $row['NomeSala']; ?></th>
							<?php endforeach; ?>
						</tr>
					</thead>
					<tbody>
						<?php
						$fasceOrarie = array_unique(array_column($speechDisponibili, 'FasciaOraria'));
						foreach ($fasceOrarie as $ora): ?>
							<tr>
								<td><?php echo $ora; ?></td>
								<?php foreach ($speechDisponibili as $speech): ?>
									<td>
										<?php if ($speech['FasciaOraria'] == $ora): ?>
											<?php foreach ($speechIscritto as $iscritto): ?>
												<?php if ($iscritto['IDProgramma'] == $speech['IDProgramma']): ?>
													<div class="speech-info">
														<span class="speech-title"><?php echo $iscritto['Titolo']; ?></span> - <?php echo $iscritto['NomeRel'] . ' ' . $iscritto['CognomeRel']; ?>
													</div>
												<?php endif; ?>
											<?php endforeach; ?>
										<?php endif; ?>
									</td>
								<?php endforeach; ?>
							</tr>
						<?php endforeach; ?>
					</tbody>
				</table>
			</div>
    	</div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
