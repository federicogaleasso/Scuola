import './App.css';

//ROUTER DOM: non è un modulo nativo, deve essere installato --> npm install react-router-dom
import {Route, BrowserRouter, Routes} from 'react-router-dom'
import Home from './Home'
import Chisiamo from './Chisiamo'
import Dovesiamo from './Dovesiamo'
import Mianavbar from './Mianavbar';

//createContext --> va importato nel file padre che contiene i figli
import { createContext } from 'react';

//createContext --> è un hooks. La funzione ritorna un componente. Serve per passare i parametri tra i figli. export permette di usare la variabile nei file
export let mioContext = createContext()

function App() {
  //Variabile globale da condividere
  let miaVariabile="Prova"

  return (
    <div className="App">
      {/* Scheletro ROUTER DOM */}
      <BrowserRouter>
        <Mianavbar/>
        {/* mioContext.Provider --> deve contenere i componenti che vogliono usare la variabile. Ha l'attributo value che contiene la variabile da condividere*/}
        {/* Per passare uno stato --> value={{dati, setDati}} */}
        <mioContext.Provider value={miaVariabile}>
          <Routes>
            {/* Route ha 2 parametri --> 1) element={<nomecomponente/>} | 2) path={"/nomesito"}*/}
            <Route element={<Home/>} path={"/"}></Route>
            <Route element={<Chisiamo/>} path={"/chisiamo"}></Route>
            <Route element={<Dovesiamo/>} path={"/dovesiamo"}></Route>
          </Routes>
        </mioContext.Provider>
      </BrowserRouter>
    </div>
  );
}

export default App;
