import React from 'react'
import "./Header.css"

const Header = (props) => { //per utilizzare i parametri --> props. Per passare il parametro --> <div>{props.pathlogo}</div>
  return (
    <div className='header'>
        <div>
            <img className="img" src={props.valori.pathlogo}/>
        </div>
        <div className='link'>
            <div><a href={props.valori.link1.url}>{props.valori.link1.anchor}</a></div>
            <div>LINK 2</div>
            <div>LINK 3</div>
        </div>
    </div>
  )
}

export default Header