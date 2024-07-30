//Galeasso Federico 20/12/2023 - Template Engine EJS

const express = require('express');
const app = express();
port = 3000;

app.set('views', './views'); //Dove si trovano i template, ovvero in views
app.set('view engine', 'ejs'); //Cosa vogliamo usare, ovvero un engine di tipo ejs

app.get('/', (req,res) => {
	let dati = "mario rossi"

	let persona={
		nome:"Mario",
		cognome:"Rossi",
		eta:47,
		cf:"GLRTAUC0246S",

	}

	//Funzione render, si trova all'interno di res. Prendo i dati, invia i dati al template, costruisce la pagina e invia la pagina al client
	//Render vs sendFile --> sendFile prende la pagina così com'è e invia al client mentre render inserisce anche il parametro
	 res.render("index",{
		//Object literal, chiave valore
		variabile1:dati,
		variabile2:persona
	 });

});

app.listen(port,()=>{

});