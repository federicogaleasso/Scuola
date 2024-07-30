//Galeasso Federico 15/11/2023 - Express

//Ha il listen, quindi non serve importare il modulo http. Eviti anche di importare il modulo fs.
let express = require('express')
const app = express()

//Middleware (o endpoint). Vuole due parametri: url, callback (req, res). Possono essere creati con la funzione get (quando l'utente digita nella barra degli indirizzi l'url), post (quando l'utente passa i parametri al server tramite il form con method POST).
app.get('/',(req,res)=>{
    res.send("Home page")
})

app.get('/pagina2',(req,res)=>{
    res.send("Io sono la seconda pagina")
})

app.get('/pagina3',(req,res)=>{
    res.sendFile(__dirname + "/html/index.html") //percorso assoluto
})

var server = app.listen(3001, ()=>{
    console.log("Server in esecuzione")
})