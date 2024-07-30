import React from 'react'
import './Home.css'
import { NavLink } from 'react-router-dom'

const Home = () => {
    return (
        <div class="contenuto">
            <h1>Benvenuto</h1>
            <p>Sei pronto a catturare i Pokemon?</p>
            <NavLink to="/pokedex"><button class="button">VAI</button></NavLink>
        </div>
    )
}

export default Home