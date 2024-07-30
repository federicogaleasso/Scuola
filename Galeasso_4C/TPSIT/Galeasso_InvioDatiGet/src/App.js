//GALEASSO FEDERICO 4C 16/3/2023 INVIO DI RICHIESTE GET/POST AL SERVER

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <form action="https://www.google.it" method="get">
        <input type="text" name="q"/>
        <input type="submit" value="INVIA"/>
      </form>
    </div>
  );
}

export default App;
