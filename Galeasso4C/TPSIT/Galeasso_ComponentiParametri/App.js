//GALEASSO FEDERICO 4C 10/11/2022 ES IN CLASSE - AGGIUNTA DI NUOVI COMPONENTI E PASSAGGIO DI PARAEMTRI

import React from 'react'
import Header from './Header' //in questo modo IMPORTIAMO il file Header.js nel componente principale

const App = () => {
  let mieiParametri={ //literal object --> contiene i parametri
    pathlogo:"https://53.fs1.hubspotusercontent-na1.net/hub/53/hubfs/image8-2.jpg?width=595&height=400&name=image8-2.jpg",
    link1:{
      url:"https://www.google.it",
      anchor:"GOOGLE"
    },
    link2:{
      url:"https://www.yahoo.it",
      anchor:"YAHOO"
    },
    link3:{
      url:"https://www.bing.it",
      anchor:"BING"
    }
  }
  return (  //con <Header/> RICHIAMIAMO il componente. PARAMETRI --> nome={""}. valori={mieiParametri} --> passiamo i parametri
    <div>
      <Header valori={mieiParametri}/>
      <div>Componente App</div>
    </div>
  )
}

export default App