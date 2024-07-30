import React, { useState, useEffect } from 'react';
import './Gcc.css';
import pokemon_icon from '../img/pokemon.png'
import 'bootstrap/dist/css/bootstrap.min.css';

function Gcc() {

  const [data, setData] = useState([]);
  const [setSelezionato, setSetSelezionato] = useState(null);
  const [searchNomeSet, setSearchNomeSet] = useState(''); // Stato per la ricerca del nome del set

  useEffect(() => {
    fetch('https://raw.githubusercontent.com/MattiaBracco05/Pokemon/main/pokemon.json')
      .then(response => response.json())
      .then(jsonData => {
        setData(jsonData);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const OpenCloseSet = (set) => {
    // Verifica se i dati del set sono già stati caricati
    if (!setSelezionato) {
      // Se non sono stati caricati, carica i dati del set selezionato
      setSetSelezionato(set);
    } else if (setSelezionato.numeroSet !== set.numeroSet) {
      // Se i dati sono stati caricati ma il set selezionato è diverso, cambia il set selezionato
      setSetSelezionato(set);
    } else {
      // Se i dati sono stati caricati e il set selezionato è lo stesso, chiudi il set
      setSetSelezionato(null);
    }
  };

  // Funzione che filtra i set in base al nome cercato
  const setFiltrato = data.filter((set) =>
    set.nomeSet.toLowerCase().includes(searchNomeSet.toLowerCase())
  );

  return (
    <div className="container-card">
       <div className="titolo">
              <h1>Gcc</h1>
            </div>
      <div className="box-ricerca">
        <div className="form-control">
          <input
            type="text"
            placeholder="Cerca"
            value={searchNomeSet}
            onChange={(e) => setSearchNomeSet(e.target.value)}
            className="input input-alt"
          />
          <span className="input-border input-border-alt"></span>
        </div>
      </div>
      <div className="row">
        {setFiltrato.map((set) => (
          <div key={set.nomeSet} className="col-lg-3 col-md-4 col-sm-12 set">
            <div>
              <img src={pokemon_icon} alt="Icona Pokemon"/>
            </div>
            <div>
              <h1>{set.nomeSet}</h1>
            </div>
            <div>
              Numero del Set: <b>{set.numeroSet}</b>
            </div>
            <div>
              Anno di Uscita: <b>{set.annoUscita}</b>
            </div>
            {setSelezionato && setSelezionato.numeroSet === set.numeroSet ? (
              <div>
                <button onClick={() => OpenCloseSet(set)} className="btn btn-danger button-figurine">CHIUDI</button>
                <div className="row">
                {set.figurine.map((pokemon) => (
                  <div key={pokemon.numero} className="col-lg-12 col-md-12 col-sm-12 figurine-card">
                    <div>
                      <img src={pokemon.url} alt={pokemon.nome} width="200" className="img-figurine"/>
                    </div>
                    <div>
                      <h2>{pokemon.nome}</h2>
                    </div>
                    <div>
                      Numero <b>{pokemon.numero}</b>
                    </div>
                    <div>
                      Stadio Evolutivo: <b>{pokemon.stadio_evolutivo}</b>
                    </div>
                    <div>
                      Abilità: <b>{pokemon.abilita.join(', ')}</b>
                    </div>
                  </div>
                ))}
                </div>
              </div>
            ) : (
              <button onClick={() => OpenCloseSet(set)} className="btn btn-success button-figurine">APRI</button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gcc;
