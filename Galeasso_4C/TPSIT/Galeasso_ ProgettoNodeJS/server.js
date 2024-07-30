//GALEASSO FEDERICO 4C 16/3/2023 NODE JS

//NodeJS (è JavaScript) permette di creare dei Web Service. Essi possono fare quello che vogliamo --> invio di immagini, streaming ecc...
//Ogni indirizzo IP ha 65000 porte.
//Per creare Web Service dobbiamo importare dei moduli
//Per vedere indirizzo IP su Linux --> ifconfig

//Importa dentro a mioServer --> http
let mioServer=require("http")

//Creazione del server sulla porta 3000. La createServer richiede come parametro una funzione callback. 2 parametri --> request(serve per far comunicare il client con il server),response(serve per far comunicare il server con il client).
mioServer.createServer((request,response)=>{
    response.setHeader("content-type","text/html")
    response.write('<form action="https://www.google.it" method="get"><input type="text" name="q"/><input type="submit" value="INVIA"/></form>')
    response.end()
}).listen(3000)