//GALEASSO FEDERICO 4C 3/11/2022 BUTTON PER STAMPARE IL NOME DEI LOCALI (file JSON)

import React, { useState } from 'react'
const URL="https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_locali.json"
const App = () => { 
  const [locali, setLocali] = useState([]);

  const connessione=()=>{ //Nuova funzione --> connessione()
    fetch(URL)
    .then((localiText)=>localiText.json())  //Scarica tutto il testo
    .then((localiJSON)=>{
      localiJSON.map((elemento, indice)=>{  //funzione map --> è un for each con 2 parametri: ELEMENTO E INDICE. Prende tutti i locali
        setLocali((locali)=>[...locali,<div>{elemento.nome} {elemento.citta}</div>])  //è una funzione call-back (ha come parametro il nome dello stato) che stampa tutti i nomi dei locali
      })
    })
  }

  return (  //button che al click richiama la funzione connessione()
    <div>
      <input type="button" value="CONNETTI OBELIX" onClick={connessione}/>
      {locali}
    </div>
  )
}

export default App