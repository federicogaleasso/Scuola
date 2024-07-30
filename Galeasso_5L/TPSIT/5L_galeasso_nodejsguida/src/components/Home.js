import React from "react";
import "./Home.css";
import { NavLink } from "react-router-dom";
import nodejs from "../img/node-js.svg"

const Home = () => {
	return (
		<div class="contenuto">
			<img src={nodejs} className="img-logo"></img>
			<h1>Benvenuto</h1>
			<p>Ti interessa scoprire ed approfondire il mondo di <strong className="green">NodeJS</strong>? Se la risposta è <strong className="green">SI</strong>, sei nel posto giusto.<br/>Qui troverai, oltre alle definizioni, esempi di codice e materiale utile per aiutarti ad approfondire e a padroneggiare l'argomento</p>
			<NavLink to="/argomenti">
				<button class="button">Iniziamo</button>
			</NavLink>
		</div>
	);
};

export default Home;
