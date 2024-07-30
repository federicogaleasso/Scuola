import React, { useState, useEffect } from 'react'

const URL = "https://raw.githubusercontent.com/andgio1976/rubrica/main/json"
let miePersone = []

const Telefono = () => {
    const [persone, setPersone] = useState([])

    const [ris, setRis] = useState([])
    const [testo, setTesto] = useState("")

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

    const Numero=(event)=> {
        setTesto(event.target.value)
    }

    const CercaTelefono=()=> {
        setRis(persone.filter((elemento) => {
            return elemento.Telefono == testo
        }))
    }

    const Stampa=()=> {
        if (ris.length > 0) {
            return <div>
                <div>
                    <div>NOME:</div><div>{ris[0].nome}</div>
                    <br/>
                    <div>COGNOME:</div><div>{ris[0].cognome}</div>
                    <br/>
                    <div>TELEFONO:</div><div>{ris[0].Telefono}</div>
                    <br/>
                </div>
            </div>
        }
    }

    return (
        <div>
            <div>
                <div>
                    <div>
                        <input type="text" placeholder="Inserisci numero di telefono" onChange={Numero}/>
                    </div>
                    <div>
                        <input type="button" value="Cerca Telefono" onClick={CercaTelefono}/>
                    </div>
                </div>
                <div>
                    {Stampa()}
                </div>
            </div>
        </div>
  )
}

export default Telefono