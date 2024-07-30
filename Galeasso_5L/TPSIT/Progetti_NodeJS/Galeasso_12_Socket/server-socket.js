//Federico Galeasso 5L 17/01/2024 - Socket

//Import del modulo net
const net = require("net")

//Server

//Creazione server, in ascolto sulla porta 4000 all'indirizzo 172.10.196.244. La callback ha solo 1 parametro: il socket.
//La funzione viene richiamata quando il client la richiama
net.createServer((socket)=>{
	//Per scrivere
	socket.write("CIAOOO!")

	//on --> nativo di Node.js, serve per gestire gli eventi (esempio: onClick in React). Ha due parametri: "data" e callback
	socket.on("data",(msg)=>{
		console.log(msg)
		console.log(socket.remoteAddress + " " + msg.toString())
	})

}).listen(4000,"172.10.196.244")

//Client

//Per il client si usa connect. 3 parametri: porta, indirizzo ip, callback.
const mioSocket = net.connect(4000, "127.0.0.1", ()=>{
	console.log("CLIENT COLLEGATO")
})

mioSocket.write("CIAOOO!")
mioSocket.on("data",(msg)=>{

})