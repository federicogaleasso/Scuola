//Import dei moduli
const http = require('http');
const socketIO = require('socket.io');
const PORT = 3000;

const server=require("http").createServer().listen(PORT)

//Inizializzazione array
let elencoNick = [];
let magazzino = [];

// Istanza di socket.io
const io = socketIO(server, {
	cors: {
		origin: '*',
	}
});

io.on('connection', (socket) => {

	// Gestione dell'evento 'invionick' (quando un client invia il nickname)
	socket.on('invionick', (data) => {
	const { nick } = data;

	// Verifica se il nome utente è unico, se sì, lo aggiunge all'elenco e lo invia a tutti i client
	if (!elencoNick.includes(nick)) {
		elencoNick.push(nick);
		io.emit('elenconick', elencoNick);
	}
	});

	// Gestione dell'evento 'inviaProdotto' (quando un client invia i dati di un prodotto)
	socket.on('inviaProdotto', (data) => {
		const { nick, nome, prezzo, quantita } = data;
		// Aggiunge le informazioni del prodotto al magazzino e lo invia a tutti i client
		magazzino.push({ nick, nome, prezzo, quantita });
		io.emit('elencomagazzino', magazzino);
	}); 

	// Gestione dell'evento 'rimuoviProdotto' (quando un client richiede la rimozione di un prodotto)
	socket.on('rimuoviProdotto', (data) => {
		const { nick, nome } = data;
		// Filtra il magazzino rimuovendo il prodotto specificato e lo invia a tutti i client
		magazzino = magazzino.filter(item => !(item.nick === nick && item.nome === nome));
		io.emit('elencomagazzino', magazzino);
	});
});