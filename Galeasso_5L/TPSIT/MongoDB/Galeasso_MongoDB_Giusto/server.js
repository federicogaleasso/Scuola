//npm install mongodb per installare il modulo di mongodb
// mern lampp mevn cerco

const { MongoClient } = require("mongodb")
const http=require("http")

//un metodo statico è che posso usare il metodo senza istanziarla
//un attributo statico è un attributo uguale per tutte le istanze quindi condiviso

//istanzio la classe MongoClient è un costruttore e gli serve l'url del server mongoDB
const client = new MongoClient("mongodb://127.0.0.1:27017")

http.createServer((req,resp)=>{

    connessione()  //mi connetto a mongoDb ma è asincrono

    const miaCollection = client.db("votidocenti").collection("voti") //apro il database valutazione e la tabella voti

    //seleziona tutti i record presenti nella collection find delete e altri ritornano una promise e devo trasformare tutti i risultati in un array
    const risultato = miaCollection.find({eta:6}).sort({nome:1}).toArray() //prende i dati e li tira fuori in json e allora li faccio in array

    //{eta:6}).sort({nome:1} ordina tutte le età per nome 1(crescente) -1(decrescente)
    //.project({nome:1}) proiezione di un solo campo tipo nome nome:1(fa vedere solo quel campo) 0(fa vedere tutti i campi tranne nome)

    miaCollection.insertOne({nome:"mario",cognome:"rossi",eta:12})

    risultato.then((dati)=>{ //tipo la fetch(una promise) i dati sono degli array
       
    })
    .finally(()=>{
        // client.close() //chiudere la connessione con il server
    })

	resp.end("xxxx")
}).listen(3000)

const connessione = async () =>{
    await client.connect() //esegue prima questa poi fa la miaCollection
}