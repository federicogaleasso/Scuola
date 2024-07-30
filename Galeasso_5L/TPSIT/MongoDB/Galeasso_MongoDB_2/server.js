//Galeasso Federico 5L 26/3/2024 - MongoDB

//Installare il modulo "mongodb"
const {MongoClient} = require("mongodb")

const http = require("http")

//Costruttore, vuole come parametro l'url
const client = new MongoClient("mongodb://localhost:27017")

http.createServer((req, res)=>{
	//Finchè non si collega al db, non esegue la riga dopo. 
	connessione()

	//Comando per apire il DB "votidocenti" e la tabella "voti". Ritorna un oggetto di nome MongoClient.
	const miaCollection = client.db("votidocenti").collection("voti")

	//Seleziona tutti i documenti presenti nella collection, funziona asincrona.
	//Tutte le funzioni find, insertOne, delete, update ecc... ritornano una PROMISE
	//$gte:5 --> cerca tutti i voti maggiori uguali di 5 ($lt --> minore; £lte --> minore uguale; $gt --> maggiore)
	//.sort{(nome:1)} --> crescente
	//.sort{(nome:-1)} --> decrescente
	//.project{(nome:0)} --> fa vedere tutti tranne nome
	//.project{(nome:1)} --> fa vedere solo nome
	const risultato = miaCollection.find({voti:{$gte:5}}).toArray()

	miaCollection.find({}).sort({cognome:1}).project({nome:1,cognome:1})

	miaCollection.insertOne({nome:"Mario",cognome:"Rossi"})
	miaCollection.insertMany([{nome:"Mario",cognome:"Rossi"},{nome:"Luca",cognome:"Verdi"}])

	miaCollection.deleteOne({cognome:"Rossi"})
	miaCollection.deleteMany({cognome:"Rossi"})

	//update --> il primo parametro è il documento (il filtro), il secondo parametro è sempre un documento, e serve per modificare.
	//L'ultimo parametro è sempre un documento --> upsert. E' un boolean (true, false). Se è false, se non c'è il documento cercato non fa nulla. Se è true, se non c'è il documento cercato lo crea.
	miaCollection.updateMany({cognome:"Rossi"},{$set:{nome:"Blu"}},{upsert:true})


	//promise. then richiama la callback. dentro a risultato c'è l'array.
	risultato.then((dati)=>{
		risultato.map(()=>{

		})
	})

	//Chiude la connessione
	.finally(()=>{
		client.close()
	})
}).listen(3000)

const connessione =async()=>{
	//Connessione a MongoDB. Connection è ascincrono, quando viene mandato in esecuzione e mongodb ha dei problemi, il server non si collega a mongodb ma esegue la riga successiva (si pianta).
	//Per questo si deve usare async await.
	await client.connect()
}