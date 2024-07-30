//Galeasso Federico 8/11/2023 - CommonJS

let http=require("http")

//Import del mio modulo
let pippo=require("./modulo")

http.createServer((req,res)=>{
    res.end(pippo.somma(5,7).toString()) //.toString() perchè la end vuole una stringa
}).listen("3000")