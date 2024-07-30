import React, { useState, useEffect } from 'react'
import './Giacenza.css';

const URL = "https://raw.githubusercontent.com/andgio1976/maga/main/info"
let miePersone = [] //dichiarazione di un'ARRAY GLOBALE al file

const Giacenza = () => {
    const [persone, setPersone] = useState([]) //creazione stato inizializzato con array vuoto

    const [pre, setPre] = useState("") //creazione stato inizializzato con stringa vuota
    const [ris2, setRis2] = useState([])    //creazione stato inizializzato con array vuoto
    const [testo2, setTesto2] = useState("")    //creazione stato inizializzato con stringa vuota

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

    const Giacenza=()=> {
        setRis2(persone.filter((elemento) => {  //filter --> è una funzione (for con if all'interno), ha un parametro (funzione callback), ritorna un'array
            console.log(elemento.giacenza)
            return (elemento.giacenza) < 3  //ritorna le giacenza minori di 3
        }))
    }

    const stampa=()=> {
        if (ris2.length > 0) {
            console.log(ris2)
            return ris2.map((elemento,index) => {
                return <div>
                <div className="d-flex justify-content-center mt-5">
                    <div>Marca:</div><div>{ris2[index].marca}</div>
                    <br/>
                    <div className="ml-5">Modello:</div><div>{ris2[index].modello}</div>
                    <br/>
                    <div className="ml-5">Giacenza:</div><div>{ris2[index].giacenza}</div>
                    <br/>
                    <div className="ml-5">Prezzo:</div><div>{ris2[index].prezzo}</div>
                    <br/>
                </div>
            </div>
            })  
        }
    }

    return (
        <div>
            <div>
                <div>
                    <div className="d-flex justify-content-center mt-5">
                        <h3>Visualizza i prodotti con giacenza minore di 3</h3>
                    </div>
                    <div className="button">
                        <input type="button" id="pulsante" value="Visualizza" onClick={Giacenza}/>
                    </div>
                </div>
                <div>
                    {ris2.length > 0 && stampa()} 
                </div>
            </div>
        </div>
    )
}

export default Giacenza