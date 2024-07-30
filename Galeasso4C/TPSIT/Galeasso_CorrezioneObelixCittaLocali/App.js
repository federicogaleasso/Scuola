import {React, useState, useEffect} from 'react'

const Citta = () => {
    const [citta, setCitta] = useState([])
    useEffect(() => {
      scarica();
    }, [])

    const miaFunzione=(parametro)=>{
        fetch("http://37.60.34.42:8080/getLocali" + new URLSearchParams({citta:parametro}))
        .then()
        .then()
    }

    const scarica=()=>{
        let mieCitta=[]
        fetch('http://37.60.34.42:8080/getCitta')
        .then((testo)=>testo.json)
        .then((mioJSON)=>{
            mioJSON.map((elemento)=>{
                mieCitta.push(<span onClick={()=>miaFunzione(elemento.id)}>{elemento.citta}</span>)
            })
            setCitta(mieCitta)
        })
    }
    

  return (
    <div>{citta}</div>
  )
}

export default Citta