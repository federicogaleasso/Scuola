import './App.css';

//ROUTER DOM: non è un modulo nativo, deve essere installato --> npm install react-router-dom
import {Route, BrowserRouter, Routes} from 'react-router-dom'

import Home from './Home'
import Chisiamo from './Chisiamo'
import Dovesiamo from './Dovesiamo'
import Mianavbar from './Mianavbar';

function App() {
  return (
    <div className="App">
      {/* Scheletro ROUTER DOM */}
      <BrowserRouter>
        <Mianavbar/>
        <Routes>
          {/* Route ha 2 parametri --> 1) element={<nomecomponente/>} | 2) path={"/nomesito"}*/}
          <Route element={<Home/>} path={"/"}></Route>
          <Route element={<Chisiamo/>} path={"/chisiamo"}></Route>
          <Route element={<Dovesiamo/>} path={"/dovesiamo"}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
