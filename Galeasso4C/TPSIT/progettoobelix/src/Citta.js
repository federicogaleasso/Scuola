import {React, useState} from 'react'

const Citta = () => {

    const URL1 = "http://37.60.34.42:8080/getLocali?citta=001"
    const URL2 = "http://37.60.34.42:8080/getLocali?citta=002"
    const [citta, setCitta] = useState([]);
    const stampaProdotti =()=>{
    let SelectId = document.querySelector("#SelectID")
    let valori = SelectId.options.selectedIndex

    if (valori == 1){
        fetch(URL1)
        .then((cittaText)=>cittaText.json())
        .then((cittaJSON)=>{
            setCitta([])
            cittaJSON.map((elemento, indice)=>{
                setCitta((citta)=>[...citta,<div><input type="radio" value="{elemento.nome}" name="citta"></input><div className='divMap'>{elemento.nome}</div></div>])
            })
        })

    } else if (valori == 2){
        fetch(URL2)
        .then((cittaText)=>cittaText.json())
        .then((cittaJSON)=>{
            setCitta([])
            cittaJSON.map((elemento, indice)=>{
                setCitta((citta)=>[...citta,<div><input type="radio" value="{elemento.nome}" name="citta"></input><div className='divMap'>{elemento.nome}</div></div>])
            })
        })

    }
}


  return (
    <div className='return'>
			<div className="select">
				<select name="" id="SelectID" onChange={stampaProdotti}>
                    <option value="">Scegli la citta</option>
					<option value="P1">Saluzzo</option>
					<option value="P2">Verzuolo</option>
				</select>
			</div>
			{citta}			
        </div>
  )
}

export default Citta