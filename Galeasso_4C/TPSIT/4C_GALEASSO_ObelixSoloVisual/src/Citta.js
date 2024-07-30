import {React, useState} from 'react'
import "../src/Citta.css"

const Citta = () => {

    const URL1 = "http://37.60.34.42:8080/getLocali?citta=001"
    const URL2 = "http://37.60.34.42:8080/getLocali?citta=002"
    const [citta, setCitta] = useState([]);
    const [locali, setLocali] = useState([]);
    const stampaProdotti =()=>{
    let SelectId = document.querySelector("#SelectID")
    let valori = SelectId.options.selectedIndex

    const handleRadioClick = (event) => {
        let selectedLocale = event.target.value;
        let apiUrl = `http://37.60.34.42:8080/getProdotti?citta_id=001&locali_id=${selectedLocale}`;
        console.log("http://37.60.34.42:8080/getProdotti?citta_id=001&locali_id=${selectedLocale}")
        fetch(apiUrl)
        .then((localiText)=>localiText.json())
        .then((localiJSON)=>{
            setLocali([])
            console.log(localiJSON)
            localiJSON.cibi.map((elemento, indice)=>{
                setLocali((locali)=>[...locali,<div><div className='divMap'>{elemento.nome}</div></div>])
            })
        })
      }
      

    if (valori == 1){
        fetch(URL1)
        .then((cittaText)=>cittaText.json())
        .then((cittaJSON)=>{
            setCitta([])
            cittaJSON.map((elemento, indice)=>{
                setCitta((citta)=>[...citta,<div className="divMap"><div className="divMap"><input type="radio" value={elemento.id} name="citta" onClick={handleRadioClick}></input><div className='divMap'>{elemento.nome}</div></div></div>])
            })
        })

    } else if (valori == 2){
        fetch(URL2)
        .then((cittaText)=>cittaText.json())
        .then((cittaJSON)=>{
            setCitta([])
            cittaJSON.map((elemento, indice)=>{
                setCitta((citta)=>[...citta,<div className="divMap"><div className="divMap"><input type="radio" value={elemento.id} name="citta"></input><div className='divMap'>{elemento.nome}</div></div></div>])
            })
        })

    }
}
  return (
    <div className='return'>
        <div className="h1"><h1>Benvenuto in OBELIX</h1></div>
			<div className="select">
				<select name="" id="SelectID" onChange={stampaProdotti}>
                    <option value="">Scegli la citta</option>
					<option value="001">Saluzzo</option>
					<option value="002">Verzuolo</option>
				</select>
			</div>
			{citta}
            {locali}		
        </div>
  )
}

export default Citta