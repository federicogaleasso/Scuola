import './App.css';

function App() {
  return (
    <div className="App">
      {process.env.REACT_APP_KEY}
    </div>
  );
}

export default App;