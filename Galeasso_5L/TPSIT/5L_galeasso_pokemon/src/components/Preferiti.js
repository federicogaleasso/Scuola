import React from 'react';
import './Preferiti.css';
import { NavLink } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Preferiti = ({ preferito, setPreferito }) => {

   // Funzione per rimuovere un Pokémon dai preferiti
  const removeFavorite = (pokemon) => {
    const aggiornaPreferiti = preferito.filter(pref => pref.numero !== pokemon.numero);
    setPreferito(aggiornaPreferiti);
    const toastId = toast.error(`Hai rimosso ${pokemon.nome} ai preferiti!`, {
      position: "top-center",
      hideProgressBar: false,
      closeButton: false,
      pauseOnHover: false,
      autoClose: 1000,
      width: "100%",
    });
    
    setTimeout(() => {
      toast.dismiss(toastId);
    }, 2000);      
  };

  return (
    <div className="container-fluid">
      <ToastContainer />
      <div className="row">
      <div className="titolo">
              <h1>Preferiti</h1>
            </div>
        {preferito && preferito.length > 0 ? (
          preferito.map((pokemon) => (
            <div key={pokemon.numero} className="col-lg-3 col-md-4 col-sm-12">
              <div className="pokemon-card">
                <img src={pokemon.img_url} alt={pokemon.nome} width="300" />
                <h1>{pokemon.nome}</h1>
                <p>Numero: <b>{pokemon.numero}</b></p>
                <p>Stadio evolutivo: <b>{pokemon.stadio_evolutivo}</b></p>
                <p>Tipo: <b>{pokemon.tipo.join(', ')}</b></p>
                <p>Debolezze: <b>{pokemon.debolezze.join(', ')}</b></p>
                <button onClick={() => removeFavorite(pokemon)} className="btn btn-danger">
                  Rimuovi dai preferiti
                </button>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="no-pokemon-preferiti">
              <h3>Non hai nessun Pokémon nei preferiti.<br />Corri a catturare il tuo primo Pokémon!</h3>
              <NavLink to="/pokedex">
                <button className="button-dark">VAI</button>
              </NavLink>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Preferiti;
