//Galeasso Federico 28/12/2023 - Compito vacanze EJS

//Import dei moduli
const express = require('express');
const app = express();
const port = 3000;

app.set('view engine', 'ejs'); //Cosa vogliamo usare, ovvero un engine di tipo ejs
app.set('views', __dirname + '/views'); //Dove si trovano i template, ovvero in views

let array_punti = [];

//Middleware 
app.use(
	express.urlencoded({
		extended: true 
	})
);

// Reindirizzamento alla pagina principale (form di inserimento punteggi)
app.get('/', (req, res) => {
  res.render('form');
});

// Gestione dei punteggi
app.post('/punti', (req, res) => {

  const nome = req.body.nome;
  const punteggio = parseInt(req.body.punteggio);

  const punteggio_esistente = array_punti.find((item) => item.nome === nome);

  // Gioco già presente
  if (punteggio_esistente) {
    punteggio_esistente.punteggio = Math.max(punteggio_esistente.punteggio, punteggio);
  } else {
    // Gioco non ancora presente
    array_punti.push({ nome, punteggio });
  }

  res.redirect('/riepilogo');
});

// Pagina di riepilogo
app.get('/riepilogo', (req, res) => {

  // Punteggio massimo, gioco con il punteggio massimo
  const punteggioMax = Math.max(...array_punti.map((item) => item.punteggio));
  const gioco_puntMax = array_punti.find((item) => item.punteggio === punteggioMax);

  res.render('riepilogo', { array_punti, punteggioMax, gioco_puntMax });
});

app.listen(port, () => {

});