import React, { useState, useEffect } from 'react';
import './Pokedex.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Pokedex = ({ preferito, setPreferito }) => {
  // Stati per gestire la lista dei Pokemon, la ricerca per nome e la ricerca per tipo
  const [pokemonList, setPokemonList] = useState([]);
  const [searchNome, setSearchNome] = useState('');
  const [searchTipo, setSearchTipo] = useState('');

  // Lista dei tipi di Pokemon
  const tipoPokemon = [
    'Erba', 'Fuoco', 'Acqua', 'Elettro', 'Ghiaccio', 'Lotta', 'Veleno', 'Terra',
    'Volante', 'Psico', 'Insetto', 'Roccia', 'Spettro', 'Drago', 'Buio', 'Acciaio', 'Folletto'
  ];

  useEffect(() => {
    fetch('https://raw.githubusercontent.com/MattiaBracco05/Pokemon/main/pokedex.json')
      .then(response => response.json())
      .then(data => {
        setPokemonList(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);


  // Funzione per aggiungere un Pokémon dai preferiti
  const aggiungiPokemonPreferito = (pokemon) => {
    if (preferito.some(pref => pref.numero === pokemon.numero)) {
      rimuoviPokemonPreferito(pokemon);
    } else {
      setPreferito([...preferito, pokemon]);
      // Alert di informazione, sparisce dopo 2 secondi
      const toastId = toast.success(`Hai aggiunto ${pokemon.nome} ai preferiti!`, {
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
    }
  };

  // Funzione per rimuovere un Pokémon dai preferiti
  const rimuoviPokemonPreferito = (pokemon) => {
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
  
  // Funzione che filtra i Pokémon in base al nome o al tipo selezionato
  const pokemonFiltrato = pokemonList.filter(pokemon => {
    const nomeTmp = pokemon.nome.toLowerCase().includes(searchNome.toLowerCase());
    const tipoTmp = searchTipo === '' || pokemon.tipo.includes(searchTipo);
    return nomeTmp && tipoTmp;
  });

  return (
    <div className="container-card">
      <ToastContainer />
            <div className="titolo">
              <h1>Pokedex</h1>
            </div>
      <div className="box-ricerca">
        <div className="form-control">
          <input
            type="text"
            placeholder="Cerca"
            value={searchNome}
            onChange={(e) => setSearchNome(e.target.value)}
            className="input input-alt"
            required=""
          />
          <span className="input-border input-border-alt"></span>
        </div>
        <select
          value={searchTipo}
          onChange={(e) => setSearchTipo(e.target.value)}
        >
          <option value="">Seleziona un tipo</option>
          {tipoPokemon.map((type) => (
            <option key={type} value={type} className="option-select">
              {type}
            </option>
          ))}
        </select>
      </div>
      <div className="row">
        {pokemonFiltrato.map(pokemon => (
          <div key={pokemon.numero} className="col-lg-3 col-md-4 col-sm-12 pokemon-card">
            <img src={pokemon.img_url} alt={pokemon.nome} width="300" />
            <div className="card-sez-down">
              <h1>{pokemon.nome}</h1>
              <p>Numero: <b>{pokemon.numero}</b></p>
              <p>Stadio evolutivo: <b>{pokemon.stadio_evolutivo}</b></p>
              <p>Tipo: <b>{pokemon.tipo.join(', ')}</b></p>
              <p>Debolezze: <b>{pokemon.debolezze.join(', ')}</b></p>
              <button
            onClick={() => aggiungiPokemonPreferito(pokemon)}
            className={`btn ${preferito.some(pref => pref.numero === pokemon.numero) ? "btn-danger" : "btn-success"}`}
          >
            {preferito.some(pref => pref.numero === pokemon.numero)
              ? "Rimuovi dai preferiti"
              : "Aggiungi ai preferiti"}
          </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Pokedex;
