//GALEASSO FEDERICO 4C 16/11/2022 COMPITO - NAVBAR CON LOGO E 4 LINK (componenti e parametri)

import React from 'react'
import Header from './Header' //in questo modo IMPORTIAMO il file Header.js nel componente principale

const App = () => {
  let mieiParametri={ //literal object --> contiene i parametri
    pathlogo:"https://static.vecteezy.com/ti/vettori-gratis/t2/622948-illustrazione-di-montagna-logo-gratuito-vettoriale.jpg",
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
    },
    link4:{
      url:"https://www.ecosia.org",
      anchor:"ECOSIA"
    }
  }
  return (  //con <Header/> RICHIAMIAMO il componente. PARAMETRI --> nome={""}. valori={mieiParametri} --> passiamo i parametri
    <div>
      <Header valori={mieiParametri}/>
    </div>
  )
}

export default App