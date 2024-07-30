import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import hamburger_icon from '../img/hamburger.png'
import pokemon_icon from '../img/pokemon.png'
import './Navbar.css'

const Navbar = () => {
  const [showNavbar, setShowNavbar] = useState(false)

  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar)
  }

  return (
    <nav className="navbar">
      <div className="container">
        <div className="logo">
        <img src={pokemon_icon} alt="" className="img_logo"/>
        </div>
        <div className="menu-icon" onClick={handleShowNavbar}>
        <img src={hamburger_icon} alt="" className="img_hamburger"/>
        </div>
        <div className={`nav-elements  ${showNavbar && 'active'}`}>
          <ul>
            <li>
              <NavLink to="/">Home</NavLink>
            </li>
            <li>
              <NavLink to="/pokedex">Pokedex</NavLink>
            </li>
            <li>
              <NavLink to="/gcc">Gcc</NavLink>
            </li>
            <li>
              <NavLink to="/preferiti">Preferiti</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar