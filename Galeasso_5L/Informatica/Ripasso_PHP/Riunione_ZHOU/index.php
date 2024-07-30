<?php
	require "./data.php";
?>
<!DOCTYPE html>
<html lang="it">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Prenotazione riunione</title>

	<link href="./bootstrap-5.3.2-dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<div class="container">
		<div class="row justify-content-center w-100">
			<div class="col-auto h1">
				Servizio di organizzazione delle riunioni
			</div>
		</div>

		<div class="row">
			<div class="col">
				<p>Benvenuto nel nostro servizio di organizzazione riunioni.</p> 
				<p>Questo servizio è uno strumento online progettato per 
				semplificare la raccolta delle disponibilità e facilitare l'organizzazione di riunioni in modo efficace.</p>
			</div>
		</div>

		<hr>

		<div class="row">
			<div class="col">
				<p>
					Inizia il processo inserendo le tue disponibilità attraverso un form interattivo. 
				</p> 
				<p>
					Seleziona i giorni della 
					settimana e le fasce orarie che meglio si adattano alla tua agenda.
				</p>
				<p>
					Inserisci il tuo nome nell'apposito campo
					testuale. Il form ti consente di specificare le tue disponibilità ad ogni invio. (Poi scegliere più di un giorno e di una fascia oraria alla volta usando CTRL-click)
				</p>
			</div>
		</div>

		<form action="registra.php" method="POST">
			<div class="row">
				<div class="col-6">
					<div class="row">
						<div class="col h4">
							Giorni
						</div>
					</div>

					<div class="row">
						<div class="col">
							<select class="form-select form-select-lg" name="giorni[]" multiple>
								<?php
									foreach($day_map as $i => $day){
								?>
									<option value=<?=$i?>><?=$day?></option>
								<?php
								}?>
							</select>
						</div>
					</div>
				</div>
				<div class="col-6">
					<div class="row">
						<div class="col h4">
							Fascia oraria
						</div>
					</div>

					<div class="row">
						<div class="col">
							<select class="form-select form-select-lg"  name="fascia[]" multiple>
								<?php
									foreach($h_map as $i => $h){
								?>
									<option value=<?=$i?>><?=$h?></option>
								<?php
								}?>
							</select>
						</div>
					</div>
				</div>
			</div>

			<div class="row mt-3">
				<div class="col-5">
					<div class="form-floating">
						<input type="text" class="form-control" name="nome" id="name" placeholder="Nome">
						<label for="name">Nome</label>
					</div>
				</div>
				<div class="col">
					<div class="row align-items-center h-100">
						<div class="col">
							<input type="button" onclick="registra()" class="btn btn-outline-primary " value="Registra"/>
						</div>
					</div>
				</div>
			</div>
		</form>
		<div class="text-danger" id="err">

		</div>
	</div>

	

	<script src="./bootstrap-5.3.2-dist/js/bootstrap.bundle.min.js"></script>
	<script>
		const form = document.querySelector("form[action='registra.php']");
		const err = document.querySelector("#err");

		const registra = () => {
			err.textContent = "";

			let name = document.querySelector("#name").value;
			
			let msg = null;
			if(name.trim().length == 0){
				msg = "Nome non inserito.";
			}else if(/\d/.test(name)){
				msg = "Nome non deve contenere numeri";
			}

			if(msg == null){
				form.submit()
			}else{
				err.textContent = msg;
			}
		}
	</script>
</body>
</html>
