import React, { useState, useEffect } from 'react'
import Giacenza from './Giacenza'
import Marca from './Marca'
import Navbar from './Navbar'
import Footer from './Footer'

const App = () => { 
    return (
        <div>
            <Navbar/>
            <Marca />
            <Giacenza />
            <Footer/>
        </div>
    )
}

export default App