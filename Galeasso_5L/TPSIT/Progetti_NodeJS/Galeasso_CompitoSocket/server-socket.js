//Federico Galeasso 5L 22/01/2024 - Compito socket

const net = require("net")
const express = require('express');
const app = express();

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))

let messaggio = ""

//Server
net.createServer((socket)=>{

	app.post('/', (req, res) => {
		messaggio = req.body.messaggio;

		socket.write(messaggio + " ")
		res.end("Messaggio inviato!")
	});

	socket.on("data",(msg)=>{
		console.log(msg)
		console.log(socket.remoteAddress + " " + msg.toString())
	})

}).listen(4000,"192.168.178.120")

app.listen(3001,()=>{

})