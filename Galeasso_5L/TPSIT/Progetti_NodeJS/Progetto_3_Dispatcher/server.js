//Galeasso Federico 8/11/2023 - Dispatcher

let http=require("http")

//Serve per parsare l'url. All'interno dell'url troviamo --> protocollo usato (http o https), mome di dominio (www.denina.it), parametri passati, come sono passati (GET o POST)
let url=require("url")

http.createServer((req,res)=>{
    let mioURL=url.parse(req.url,true)
    switch (mioURL.path) {
        case "/":
            res.end("Home Page")
            break;
        case "/pluto":
            res.end("Pluto")
            break;
        case "/topolino":
            res.end("Topolino")
            break;
    
        default:
            break;
    }
}).listen("3000")