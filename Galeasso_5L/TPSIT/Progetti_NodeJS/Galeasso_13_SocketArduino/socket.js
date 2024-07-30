//Federico Galeasso 5L 24/01/2024 - Socket Arduino

const net = require("net")
const express = require('express');
const app = express();

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))

let carattere = ""

//Client
const mioSocket = net.connect(4000, "172.10.196.150", ()=>{
	console.log("CLIENT COLLEGATO")
})

app.post('/', (req, res) => {
	carattere = req.body.carattere;

	mioSocket.write(carattere + " ")
	res.end("Messaggio inviato!")
});

app.listen(3001,()=>{

})