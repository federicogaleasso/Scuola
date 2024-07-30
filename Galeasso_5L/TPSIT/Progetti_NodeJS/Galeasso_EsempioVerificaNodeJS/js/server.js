import http from 'http'
import url from 'url'
import { somma, differenza, divisione, moltiplicazione } from './modulo.js'
const port = 3001

http.createServer((req, res)=>{
    let parametri = url.parse(req.url, true)
    let num1 = parseInt(parametri.query.primo)
    let num2 = parseInt(parametri.query.secondo)
    let operazione = parametri.query.operation

    switch (operazione) {
        case "Somma":
            res.end(somma(num1, num2).toString())
            break
        
        case "Sottrazione":
            res.end(differenza(num1, num2).toString())
            break

        case "Divisione":
            res.end(divisione(num1, num2).toString())
            break
        
        case "Moltiplicazione":
            res.end(moltiplicazione(num1, num2).toString())
            break
    
        default:
            res.end("errore")
            break
    }

}).listen(port)
