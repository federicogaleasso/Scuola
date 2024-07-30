import React, { useState, useEffect } from 'react'
import './Marca.css';

const URL = "https://raw.githubusercontent.com/andgio1976/maga/main/info"
let miePersone = [] //dichiarazione di un'ARRAY GLOBALE al file

const Marca = () => {
    const [persone, setPersone] = useState([])  //creazione stato inizializzato con array vuoto

    const [ris, setRis] = useState([])  //creazione stato inizializzato con array vuoto
    const [testo, setTesto] = useState("") //creazione stato inizializzato con stringa vuota

    useEffect(() => {
        connessione();  //richiama la funzione una sola volta. in questo modo si evita il loop infinito
    }, [])
      
  
    const connessione=()=>{
        fetch(URL)
        .then((testo) => testo.json())
        .then((mioJSON) => {
            mioJSON.map((elemento) => {
                miePersone.push(elemento)
            })
            setPersone(miePersone)  //memorizzazione dell'ARRAY nello STATO
        })
    }

    const Numero=(event)=> {    //event --> parametro, contiene il testo e le caratteristiche della casella di testo
        setTesto(event.target.value)    //recupera il carattere digitato
    }

    const cercaMarca=()=> {
        setRis(persone.filter((elemento) => {   //filter --> è una funzione (for con if all'interno), ha un parametro (funzione callback), ritorna un'array
            return elemento.marca == testo  //ritorna la marca nel file json uguale che abbiamo digitato
        }))
    }

    const Stampa=()=> {
        if (ris.length > 0) {
            return <div>
                <div className="d-flex justify-content-center mt-5">
                    <div>Marca:{ris[0].marca}</div>
                    <div className="ml-5">Modello:{ris[0].modello}</div>
                    <br/>
                    <div className="ml-5">Giacenza:{ris[0].giacenza}</div>
                    <br/>
                    <div className="ml-5">Prezzo:{ris[0].prezzo}</div>
                    <br/>
                </div>
            </div>
        }
    }

    return (
        <div>
            <div>
                <div>
                    <div className="d-flex justify-content-center mt-5">
                        <h3>Visualizza i prodotti cercando la loro marca</h3>
                    </div>
                    <div className='text'>
                        <input type="text" id="casella" placeholder="Inserisci la marca" onChange={Numero}/>
                    </div>
                    <div className='button'>
                        <input type="button" id="pulsante" value="Visualizza" onClick={cercaMarca}/>
                    </div>
                </div>
                <div>
                    {Stampa()}
                </div>
            </div>
        </div>
  )
}

export default Marca