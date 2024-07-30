import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import hamburger_icon from '../img/bars-solid.svg'
import nodejs_icon from '../img/node-js.svg'
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
        <NavLink to="/"><img src={nodejs_icon} alt="" className="img_logo"/></NavLink>
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
              <NavLink to="/argomenti">Argomenti</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar