import React from 'react'
import {NavLink, useNavigate} from 'react-router-dom'

const Mianavbar = () => {

    //Serve per passare da un componente ad un altro
    const pippo=useNavigate()
    const apri=()=>{
        pippo("/")
        //Le informazioni possono essere salvate nel browser. Il browser ha 2 memorie: local storage e session storage.
        //Per vedere le informazioni salvate --> ispeziona --> archiviazione (italiano), storage (inglese) --> local / session storage
        localStorage.setItem("Variabile Local Storage", "Federico")
        sessionStorage.setItem("Variabile Session Storage", "Galeasso")
    }

  return (
    <div>
        {/* NavLink ha un parametro --> to={"/"}; {-1} torna indietro */}
        <NavLink to={"/"}>Home</NavLink><br/>
        <NavLink to={"/chisiamo"}>Chi siamo</NavLink><br/>
        <NavLink to={"/dovesiamo"}>Dove siamo</NavLink><br/>
        <NavLink to={-1}>Indietro</NavLink><br/><br/>
        <input type="button" value="Torna alla HOME" onClick={apri}></input><br/><br/>
    </div>
  )
}

export default Mianavbar