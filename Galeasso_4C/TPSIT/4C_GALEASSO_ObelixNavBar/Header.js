import React from 'react'
import "./Header.css"

const Header = (props) => { //per utilizzare i parametri --> props. Per passare il parametro --> <div>{props.pathlogo}</div>
  return (
    <div className='header'>
        <div>
            <img className="img" src={props.valori.pathlogo}/>
        </div>
        <div className='link'>
            <div className='div-link1'><a className='link1' target="blank" href={props.valori.link1.url}>{props.valori.link1.anchor}</a></div>
            <div className='div-link2'><a className='link2' target="blank" href={props.valori.link2.url}>{props.valori.link2.anchor}</a></div>
            <div className='div-link3'><a className='link3' target="blank" href={props.valori.link3.url}>{props.valori.link3.anchor}</a></div>
            <div className='div-link4'><a className='link4' target="blank" href={props.valori.link4.url}>{props.valori.link4.anchor}</a></div>
        </div>
    </div>
  )
}

export default Header