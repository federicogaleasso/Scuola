import React from 'react'
import './Navbar.css';

const Navbar = () => {
  return (
    <div className='Navbar'>
        <div>
            <img className="img" src={"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1200px-Google_%22G%22_Logo.svg.png"}/>
        </div>
        <div className='link'>
            <div className='div-link1'><a className='link1' target="blank" href="https://www.google.it/">GOOGLE</a></div>
        </div>
    </div>
  )
}

export default Navbar