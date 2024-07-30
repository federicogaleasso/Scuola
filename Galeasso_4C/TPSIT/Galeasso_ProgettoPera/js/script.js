const visualizza=()=>{
    
    const url="https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"

    fetch(url)  //FUNZIONE fetch() --> scarica tutto il contenuto di una pagina web. Richiede 2 parametri: URL, LITERAL OBJECT

        .then((dati)=>dati.json()) //Quando la fetch() ha finito di scaricare tutti i dati, viene richiamata la PRIMA funzione .then() --> all'interno c'è la variabile che contiene tutti i dati e li trasforma in JSON

            .then((datiJSON)=>{ //La SECONDA funzione .then() --> carica tutti i dati JSON nella nostra pagina web
                let nuovoElemento=document.createElement("div") //Crea il tag DIV
                nuovoElemento.innerHTML=datiJSON[0].data.sensor1.lowRes.temperature  //All'interno del DIV inseriamo temperatura ecc...
                document.querySelector("body").appendChild(nuovoElemento)    //In questo modo inseriamo nel body il file JSON
            })

    let mioLiteral={    //LITERAL OBJECT
        nome:"Mario",
        cognome:"Rossi",
        eta:50,
        telefono:{
            cellulare:339852656,
        }
    }

    console.log(mioLiteral.telefono.cellulare)  //In console stampa il contenuto di "cellulare" che si trova all'interno dell'oggetto "telefono", che a sua volta si trova nell'oggetto "mioLiteral"

    let mioArry = new Array();  //Creazione di un ARRAY
    mioLiteral.nome="Federico"  //Federico al posto di Mario
    mioLiteral.cognome="Galeasso"   //Galeasso al posto di Rossi
    mioLiteral.eta=17   //17 al posto di 50

    mioArry.push(mioLiteral)    //Stampa tutto l'array
    console.log(mioArry[0].nome)    //stampa il nome, che si trova nell'array 
}