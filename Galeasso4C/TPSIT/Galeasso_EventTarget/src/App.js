import './App.css';

function App() {

  const cliccami=(event)=>{
    alert(event.target.dataset.prezzo) //target --> viene messo sul div padre e l'evento viene ereditato dai figli. Fa vedere il contenuto del div dove abbiamo cliccato
    
    //currentTarget --> viene messo sul div padre. Recupera SOLO il tag del div padre

    event.target.style.border="10px dotted green"
  }

  return (
      <>
        <div onClick={cliccami}>
          <img data-prezzo="3000.00 €" style={{width:"10%"}} src="https://m.media-amazon.com/images/I/51JYUf-PzjL._AC_SL1200_.jpg"></img> {/* data-prezzo --> attributo personalizzato */}
          <img data-prezzo="500.00 €" style={{width:"10%"}} src="https://m.media-amazon.com/images/I/61La8PAa42L._AC_SL1500_.jpg"></img>
          <img data-prezzo="350.00 €" style={{width:"10%"}} src="https://m.media-amazon.com/images/I/61vkJ9V6-dL._AC_SL1500_.jpg"></img>
        </div>
      </>
  );
}

export default App;