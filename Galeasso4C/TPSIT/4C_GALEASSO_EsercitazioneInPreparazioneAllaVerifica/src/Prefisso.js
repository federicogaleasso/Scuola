import React, { useState, useEffect } from 'react'

const URL = "https://raw.githubusercontent.com/andgio1976/rubrica/main/json"
let miePersone = []

const Prefisso = () => {
    const [persone, setPersone] = useState([])

    const [pre, setPre] = useState("")
    const [ris2, setRis2] = useState([])
    const [testo2, setTesto2] = useState("")

    useEffect(() => {
        connessione();
    }, [])
      
  
    const connessione=()=>{
        fetch(URL)
        .then((testo) => testo.json())
        .then((mioJSON) => {
            mioJSON.map((elemento) => {
                miePersone.push(elemento)
            })
            setPersone(miePersone)
        })
    }

    const Prefisso=(event)=> {
        setTesto2(event.target.value)
    }

    const CercaPrefisso=()=> {
        setRis2(persone.filter((elemento) => {
            return (elemento.Telefono[0] + elemento.Telefono[1] + elemento.Telefono[2] + elemento.Telefono[3]) == testo2
        }))
    }

    const stampa=()=> {
        if (ris2.length > 0) {
            return ris2.map((elemento) => {
                return <div>
                    <div>
                        <div>NOME:</div><div>{elemento.nome}</div>
                        <br/>
                        <div>COGNOME:</div><div>{elemento.cognome}</div>
                        <br/>
                        <div>TELEFONO:</div><div>{elemento.Telefono}</div>
                        <br/>
                        <div>CITTÀ:</div> <div>{elemento.citta}</div>
                    </div>
                    <div></div>
                </div>
            })  
        }
    }

    return (
        <div>
            <div>
                <div>
                    <div>
                        <input type="text" placeholder="Inserisci prefisso" onChange={Prefisso}/>
                    </div>
                    <div>
                        <input type="button" value="Cerca Prefisso" onClick={CercaPrefisso}/>
                    </div>
                </div>
                <div>
                    {ris2.length > 0 && stampa()} 
                </div>
            </div>
        </div>
    )
}

export default Prefisso