//GALEASSO FEDERICO 4C 26/10/2022 STATI E VARIABILI

import React, { useState, useEffect } from 'react'
const App = () => {
  const [msgPera, setmsgPera] = useState(""); //dichiarazione stato. PARAM 1 --> è lo stato. PARAM 2 --> modifica lo stato, DEVE cominciare con set. PARAM 3 --> inizializzazione a ""
  const URL="https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"

  const scarica=()=>{
    fetch(URL)
    .then((testo)=>testo.json())
    .then((pera)=>{
      setmsgPera(pera[0].data.sensor1.lowRes.humidity + " " + pera[0].data.sensor1.lowRes.temperature)  //Ricarica lo stato con umidità e temperatura
    })
  }

  return (
    <div>{msgPera}{scarica()}</div> //{msgPera} --> stampa a video msgPera (tmp e umidità). {scarica()} --> richiama la funzione
  )
}

  //!!!COPIARE questo codice (da riga 21 a 40) dentro alla FUNZIONE App per vedere il FUNZIONAMENTO!!!
  const URL="https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"
  const [arrayPera, setArrayPera] = useState([]);
  useEffect(() => { //richiama una funzione, in questo caso richiama scarica una solo volta con []. QUESTO EVITA IL LOOP INFINITO!
    scarica()
  }, [])
  
  const scarica=()=>{
    fetch(URL)
    .then((testo)=>testo.json())
    .then((pera)=>{
      pera.map((elemento, indice)=>{  //funzione map, è un for each e scarica tutte le temperature e tutte le umidità
        setArrayPera((arrayPera)=>[...arrayPera,<div>{elemento.data.sensor1.lowRes.humidity + " " + elemento.data.sensor1.lowRes.temperature}</div>]) //creiamo una funzione callback con arrayPera come paramentro. Dopo copiamo il nuovo elemento dentro al contenuto dell'array dello stato stato se non mettiamo ... troviamo solo l'ultimo elemento
      })
    })
  }

  return (
    <div>{arrayPera}</div>
  )

export default App