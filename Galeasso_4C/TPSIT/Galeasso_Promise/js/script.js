const visualizza=()=>{
    const primaFunzione=async()=>{
        sleep(3000)
        console.log("Io sono la prima funzione") //Funzione ASINCRONA --> async
        return "scaricato"
    }

    const secondaFunzione=()=>{
        console.log("Io sono la seconda funzione")  //Funzione SINCRONA
    }

    primaFunzione()
    .then((parametro)=>{    //PROMISE
        //elaborazione...
    })

    secondaFunzione();
}