//GALEASSO FEDERICO 4C 5/11/2022 COMPITO - STAMPA DEI NOMI DELLE CITTÀ E IL LORO STEMMA (file JSON)

import React, { useState } from 'react'
import "../src/App.css"

const URL="https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_citta_fake.json"
const App = () => { 
  const [citta, setCitta] = useState([]);
  const stampa=()=>{
    fetch(URL)
    .then((cittaText)=>cittaText.json())
    .then((cittaJSON)=>{
      cittaJSON.map((elemento, indice)=>{
        if(indice==0){
          setCitta((citta)=>[...citta,<div className='header'>{elemento.citta}<div className='border'><img src="https://comune.saluzzo.cn.it/wp-content/uploads/sites/18/2019/01/saluzzoStemmaTrasparente400.png" width="70" height="70"/></div></div>])
        }
        if(indice==1){
          setCitta((citta)=>[...citta,<div className='header'>{elemento.citta}<div className='border'><img src="https://www.comune.verzuolo.cn.it/logo_tratto.png" width="70" height="70"/></div></div>])
        }
      })
    })
  }

  return (
    <div className='return'>
      <div className='button'>
        <input type="button" id="pulsante" value="CLICCA PER STAMPARE CITTÀ E STEMMI" onClick={stampa}/>
      </div>
      {citta}
    </div>
  )
}

export default App