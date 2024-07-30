//GALEASSO FEDERICO 4C 22/3/2023 PRIMO COMPITO NODE JS

//NodeJS (è JavaScript) permette di creare dei Web Service. Essi possono fare quello che vogliamo --> invio di immagini, streaming ecc...
//Ogni indirizzo IP ha 65000 porte.
//Per creare Web Service dobbiamo importare dei moduli
//Per vedere indirizzo IP su Linux --> ifconfig

//Importa dentro a mioServer --> http
let mioServer=require("http")

let mioUrl=require("url")

//Data e ora corrente
const now = new Date();
const dateTimeString = now.toLocaleString();

//Creazione del server sulla porta 3000. La createServer richiede come parametro una funzione callback. 2 parametri --> request(serve per far comunicare il client con il server),response(serve per far comunicare il server con il client).
//Per startare: nodejs nomeserver.js
mioServer.createServer((request,response)=>{
    let miaData=new Date()
    let xxx=mioUrl.parse(request.url,true)
    console.log(xxx.query.parametro)
    response.setHeader("content-type","text/html")
    response.write("<strong>xxxxhjgf hjgf yhj gf" + miaData.toLocaleDateString()+ "</strong>")
    response.end()
}).listen(3000)