import './App.css';
import React, { useState } from 'react'

function App() {

  const [sport, setSport] = useState([])

  const aggiornaRadio =(event)=>{
    console.log(event.target.value)
  }

  const aggiornaCheckBox =(event)=>{
    //Con questo if controlliamo se l'utente ha già premuto il checkbox: se è già stato premuto (ad esempio) il checkbox "Basket", non lo ristampa.
    //includes ritorna una boolean (True o False)
    if(!sport.includes(event.target.value)){
      setSport([...sport,event.target.value])
    } else{
      //Qua invece, se premiamo sul checkbox "Basket" e lo ripremiamo, "Basket" viene eliminato grazie alla filter
      //filter ritorna un array in base alla condizione
      setSport(sport.filter((elemento)=>elemento!=event.target.value))
    }
  }

  return (
    <div className="App">
      <div onChange={aggiornaRadio}>
        <input type="radio" name="sesso" id="" value={"maschio"}/>
        <input type="radio" name="sesso" id="" value={"femmina"}/>
      </div>

      <div onChange={aggiornaCheckBox}>
        <input type="checkbox" name="hobby" value={"Basket"}/>
        <input type="checkbox" name="hobby" value={"Calcio"}/>
        <input type="checkbox" name="hobby" value={"Tennis"}/>
        {sport}
      </div>
    </div>
  );
}

export default App;