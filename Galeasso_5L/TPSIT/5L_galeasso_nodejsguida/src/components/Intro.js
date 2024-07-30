import React, { useEffect } from 'react';
import './Intro.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import hljs from 'highlight.js';
import 'highlight.js/styles/base16/onedark.css';

const Intro = () => {

	useEffect(() => {
		hljs.highlightAll();
	}, []);
	
const codice1 = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</p>
    </br>
    <a href="https://www.google.it/">Google</a>
    </br>
    <img src="..."/>
</body>
</html>`;

const codice2 = `//Import del modulo "http"
let http = require("http")

//Import del modulo "fs". Serve per operare sul filesystem
let fs = require("fs")

//Per startare: node nomefile.js. Avviato, il server resta sempre in ascolto. Per aggiornamento automatico: nodemon nomefile.js.
//Per chiudere: CTRL + C
//Creazione del server, con parametri "request" e "response", in ascolto sulla porta 3000
//Request: comunicazione tra CLIENT e SERVER
//Response: comunicazione tra SERVER e CLIENT

http.createServer((req,res)=>{

    //Codice
    res.setHeader('content-type', 'text/html')
    // res.write("<strong>Benvenuto</strong>"); // Appende il testo o l'html all'interno del pacchetto.
    let contenutoFile = fs.readFileSync("./index.html") // Finchè non vengono caricati tutti i dati, l'end non viene richiamato
    res.end(contenutoFile); // Prende il pacchetto e lo invia al client.
    
}).listen("3000")`;

  return (
    <div className="container-fluid">
    	<div className="div-intro">
			<h1>Introduzione</h1>
			<br/>
			<h4>Cos'è NodeJS?</h4>
			<p>
NodeJS è un framework che viene utilizzato con AngularJS, ReactJS e MongoDB e serve per creare dei servizi.
Un servizio è un programma che esegue determinate istruzioni (<i>es: inviare la data corrente</i>).<br/>
Il server recupera quindi la chiave primaria e memorizza il record all'interno di una tabella.<br/>
Il linguaggio di programmazione utilizzato è JavaScript lato server: gira sul server e invia la pagina al client. Essa viene aperta dall'utente tramite il browser, che interpreta la pagina solamente come HTML, CSS e JS.<br/><br/>
<h4>Libreria o Framework?</h4>
La principale differenza tra libreria e framework è che la libreria deve essere importata, mentre il framework è un ambiente.<br/><br/>
<h4>Cos'è NPM?</h4>
NPM è un portale che contiene moduli e componenti già fatti.<br/><br/>
<h4>Il compito del browser</h4>
Il client per comunicare con il server DEVE usare il browser.<br/>
L'header della risposta del pacchetto dice al browser come comportarsi, mentre l'header della richiesta contiene informazioni, come la lingua.<br/>
HTTP nasce come protocollo senza stato (stateless), ovvero senza memoria. Non salva le informazioni.<br/>
Il browser può salvare la pagina web nella cache, in modo da non dover ricaricare ogni volta la pagina. Se però il campo lenght cambia, e quindi vuol dire che è cambiato qualcosa, la pagina viene ricaricata.<br/><br/>
<h4>Creazione di un Server Web (<a href="https://github.com/federicogaleasso/NodeJS/blob/main/Progetto_1.zip" target="_blank">scarica il progetto qui</a>)</h4>
Ecco come si crea un Server Web (nota: Il codice viene interpretato dal server e non dal browser):
			</p>
<i>index.html</i>
<pre className="outside-code-toolbar">
<code className="language-html inside-code-toolbar">
{codice1}
</code></pre>
<i>server.js</i>
<pre className="outside-code-toolbar">
<code className="language-javascript inside-code-toolbar">
{codice2}
</code></pre>
		</div>
		
    </div>
  );
};

export default Intro;
