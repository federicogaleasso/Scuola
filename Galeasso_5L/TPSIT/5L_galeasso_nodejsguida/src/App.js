// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Argomenti from './components/Argomenti';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Footer from './components/Footer';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/argomenti" element={<Argomenti />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
