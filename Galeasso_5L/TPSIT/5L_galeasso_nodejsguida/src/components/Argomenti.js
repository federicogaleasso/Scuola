import React, { useState, useEffect } from 'react';
import './Argomenti.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Intro from './Intro';


const Argomenti = () => {
  return (
    <div className="container">
    	<Intro />
    </div>
  );
};

export default Argomenti;
