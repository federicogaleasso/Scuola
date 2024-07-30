//Galeasso Federico 5L 25/10/2023 - Passaggio di parametri al server

let http = require("http")
let fs = require("fs")
// const querystring = require('querystring'); // Deprecato!
const querystring = require('url');

http.createServer((req,res)=>{

    //Codice

    let parametro = querystring.parse(req.url,true)
    res.end(parametro.query.cognome)
    //res.end(req.url); // Contiene l'url che il client ha inviato al server

}).listen("3000")