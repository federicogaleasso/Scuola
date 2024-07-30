// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Pokedex from './components/Pokedex';
import Preferiti from './components/Preferiti';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Footer from './components/Footer';
import Gcc from './components/Gcc';

function App() {
  // Inizializzazione dello stato dei preferiti con un array vuoto
  const [preferito, setPreferito] = useState([]);

  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/pokedex"
            element={<Pokedex preferito={preferito} setPreferito={setPreferito} />}
          />
          <Route path="/gcc" element={<Gcc />} />
          <Route
            path="/preferiti"
            element={<Preferiti preferito={preferito} setPreferito={setPreferito} />}
          />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
