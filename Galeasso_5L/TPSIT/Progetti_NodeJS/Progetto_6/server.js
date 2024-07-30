import http from "http"
import url from "url"
import {differenza,somma} from "./modulo.js"

http.createServer((req,res)=>{
    let parametro = url.parse(req.url,true)
    let num1 = parseInt(parametro.query.numero1)
    let num2 = parseInt(parametro.query.numero2)
    let operazione = parametro.query.operazione

    switch (operazione) {
        case "Somma":
            res.end(somma(num1,num2).toString())
            break;
        case "Sottrazione":
            res.end(differenza(num1,num2).toString())
            break;
        default:
            break;
    }
}).listen("3000")