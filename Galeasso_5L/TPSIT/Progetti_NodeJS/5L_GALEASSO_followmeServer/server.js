//Galeasso Federico 5L 6/02/2024 - Server FollowMe

const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))

// Endpoint home
app.get('/', (req, res) => {
	res.setHeader('content-type', 'text/html')
    let home = fs.readFileSync("./index.html")
    res.end(home);
});

// Endpoint getDirections
app.post('/getDirections', (req, res) => {
	let plesso = req.body.plesso
    let sorgente = req.body.sorgente
    let destinazione = req.body.destinazione
	res.send("/getDirections")
});

// Endpoint showAll
app.post('/showAll', (req, res) => {
	let plesso = req.body.plesso
	res.send("/showAll")
});

app.listen(port, () => {});