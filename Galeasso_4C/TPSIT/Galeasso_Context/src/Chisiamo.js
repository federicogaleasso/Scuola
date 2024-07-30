//useContext va importato da react
import React, { useContext } from 'react'

//mioContext va importato da App.js
import { mioContext } from './App.js'

const Chisiamo = () => {
  //Variabile. useContext --> vuole il nome del createContext (in questo caso mioContext)
  let messaggio=useContext(mioContext)
  return (
    <div>{messaggio}</div>
  )
}

export default Chisiamo