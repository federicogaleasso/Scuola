const server=require("http").createServer().listen(3000)
let elencoNick=[]
let messaggio=[]

const io = require('socket.io')(server, {
	cors: {
		origin: '*',
	}
});

io.on("connection",(socketClient)=>{
    socketClient.on("invionick",(dati)=>{
		if(!elencoNick.includes(dati)){
			elencoNick.push(dati)
		}
		console.log('Nickname: ' + dati)
		socketClient.emit("elenconick",elencoNick)
    })

	socketClient.on("inviomex",(message)=>{
		messaggio.push(message)
		console.log('>> ' + message)
		io.emit("messaggio_inviato", messaggio)
	})   
})