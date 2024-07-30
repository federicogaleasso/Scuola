import React, { useState } from 'react'
import Navbar from "./Navbar"
const URL="https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_locali.json"

let mieiLocali=new Array() //dichiarazione di un'ARRAY GLOBALE al file

const App = () => {

const [locali, setLocali] = useState([])
const [testo, setTesto] = useState("")
const [risultato, setRisultato] = useState([])

const connessione=()=>{
  fetch(URL)
  .then((testo)=>testo.json())
  .then((mioJSON)=>{
    mioJSON.map((elemento)=>{
      mieiLocali.push(elemento)
    })
    setLocali(mieiLocali) //memorizzazione dell'ARRAY nello STATO
  })
}

const ricerca =(event)=>{ //event --> parametro, contiene il testo e le caratteristiche della casella di testo
  setTesto(event.target.value) //recupera il carattere digitato
}

const cerca =()=>{
  setRisultato(locali.filter((elemento)=>{ //filter --> è una funzione (for con if all'interno), ha un parametro (funzione callback), ritorna un'array
    return elemento.nome == testo // ritorna gli elementi del json uguali a quello che abbiamo digitato
  }))
}

  return (
    <div>
      <input type="button" value={"CONNETTI OBELIX"} onClick={connessione}/>
      <div>
        <input type="text" name="" id="" placeholder="Inserisci la città" onChange={ricerca}/>  {/**onChange --> è un'evento*/}
        <input type="button" value="CERCA" onClick={cerca}/>
      </div>
      <div>
        {risultato.length>0 && risultato[0].nome} {/*Non può stampare il nome della città senza aver prima cliccato su CONNETTI OBELIX. Per ovviare, controlliamo se la lunghezza dell'array è > 0 e se lo è stampa il nome del json relativo al nome che abbiamo inserito nella casella di testo*/}
      </div>
    </div>
    
  )
}

export default App