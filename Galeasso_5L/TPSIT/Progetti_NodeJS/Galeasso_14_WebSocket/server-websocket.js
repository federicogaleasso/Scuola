//Galeasso Federico 5L 31/01/2024 - WebSocket

//npm install socket.io
//Socket.io non ha la funzione listen, quindi deve essere usato con http o express.
let server = require("http").createServer().listen("3000")

let io = require("socket.io")(server,{
	cors:{
		origin:"*"
	}
})

//Evento, funzione callback. Richiamata quando il client instaura la connessione.
io.on("connection",(socketConClient)=>{
	
	socketConClient.on("invia", (dati)=>{
		
		//Emit crea l'evento, la funzione on lo recupera.
		socketConClient.brodcast.emit("pippo", dati)
	})
})