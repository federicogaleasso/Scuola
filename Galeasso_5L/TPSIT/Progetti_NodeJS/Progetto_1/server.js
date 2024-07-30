//Galeasso Federico 5L 18/10/2023 - Creazione primo server

//Se da errore sui permessi per eseguire script: https://turbolab.it/windows-10/come-attivare-abilitare-esecuzione-script-.ps-powershell-impossibile-caricare-file.-esecuzione-script-disattivata-sistema-uso-aboutexecutionpolicies-966

//Import del modulo "http"
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
    
}).listen("3000")