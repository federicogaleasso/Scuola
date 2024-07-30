//Galeasso Federico 8/11/2023 - ES modules

import http from "http"
import {differenza,somma} from "./modulo.js"

http.createServer((req,res)=>{
    res.end(somma(5,7).toString())
}).listen("3000")