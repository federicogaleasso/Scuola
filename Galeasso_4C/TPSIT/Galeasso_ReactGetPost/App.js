import React, {useState} from 'react'

const URL=""

const App = () => {
  const [first, setfirst] = useState("")

fetch(
  'https://www.amazon.it/getLocali' + new URLSearchParams({ //in questo modo inviamo all'URL i parametri in GET (i parametri sono nell'url). new URLSearchParams --> serve a concatenare i parametri al link
    idCitta:"P001",
  })
)
.then((pippo)=>pippo.json)
.then((mioJSON)=>{
  //...
})

let data={citta:'001', idLocali:"P007"} //parametri inviati al server
fetch(
  'https://www.amazon.it/getLocali',{ //in questo modo inviamo all'URL i parametri in POST (i parametri sono nel pacchetto, non nell'url). fetch --> param 1 (url), param 2 (object literal)
    method:"POST",
    headers:{
      'Content-Type':'application/json',
    },
    body:JSON.stringify(data),  //lo stringify trasforma in stringa, in questo caso tarsforma il json in stringa
  }
)
.then((pippo)=>pippo.json)
.then((mioJSON)=>{
  //...
})

  return (
    <div>
      <input type="text"></input>
      <input type="button" value="INVIA"></input>
    </div>
  )
}

export default App