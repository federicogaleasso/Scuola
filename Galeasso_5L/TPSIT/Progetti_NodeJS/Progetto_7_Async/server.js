//Galeasso Federico 15/11/2023 - Async e Await

const somma=async()=>{ //async --> la funzione RIMANE SINCRONA, non trasforma la funzione in asincrona. Permette di usare await e di avere il then.
    await fetch('https://v2.jokeapi.dev/joke/Programming?type=single') //await --> la funzione deve essere dichiarata con async, ritorna una promise e permette di utilizzare then, catch, e finally.
    .then(res => res.json())
    .then(json => console.log(json.joke))
}

somma().then(console.log("Hello World!")) //solo dopo che ha eseguito la funzione somma stamperà il console.log