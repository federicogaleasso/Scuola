//Galeasso Federico 20/12/2023 - Recupero parametri EJS

const express = require('express');
const app = express();
port = 3000;

app.set('views', './views'); //Dove si trovano i template, ovvero in views
app.set('view engine', 'ejs'); //Cosa vogliamo usare, ovvero un engine di tipo ejs

app.use(express.json());
app.use(
    express.urlencoded({
        extended: true,
    })
);

app.post("/recupera",(req,res)=>{
	let persona={
		nome:req.body.nome,
		cognome:req.body.cognome,
		cf:req.body.cf,

	}

	//Funzione render, si trova all'interno di res. Prendo i dati, invia i dati al template, costruisce la pagina e invia la pagina al client
	//Render vs sendFile --> sendFile prende la pagina così com'è e invia al client mentre render inserisce anche il parametro
	res.render("index",{
		//Object literal, chiave valore
		variabile:persona
	 });
})

app.listen(port,()=>{

});