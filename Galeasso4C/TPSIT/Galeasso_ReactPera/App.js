//JSON Tabella Pera in React con la fetch

import React from 'react'

const App = () => {
  
  const URL="https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"

  const scarica=()=>{
    fetch(URL)
    .then((testo)=>testo.json())
    .then((pera)=>{
      let miaVariabile=pera[0].data.sensor1.lowRes.humidity + " " + pera[0].data.sensor1.lowRes.temperature
      console.log(miaVariabile)
    })
  }

  return (
    <div>{scarica()}</div>
  )
}

export default App