import './App.css';
import React, { useRef } from 'react'

function App() {
  //È un HOOKS --> serve per recuperare un tag (come il querySelector)
  const mioDiv = useRef(null)

  const cambiaColore=()=>{
    console.log(mioDiv) //possiamo vedere in console tutte le proprietà
    mioDiv.current.style.color="red"  //cambia il colore
    mioDiv.current.textContent="CIAO" //cambia la scritta in "CIAO"
    mioDiv.current.style.backgroundColor="orange" //cambia lo sfondo
    mioDiv.current.style.fontSize="50px"  //cambia la dimensione
  }

  return (
    <>
      <div ref={mioDiv}>
        {'BENVENUTO'}
      </div>
      <input type="button" value="COLORE" onClick={cambiaColore}/>
    </>
  );
}

export default App;