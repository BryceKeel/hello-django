import './App.css'
import React from 'react';
import ApiComponent from './ApiComponent';

function App() {
  const refreshPage = () => {
    window.location.reload();
  };

  return (
    <div className="App">
      <div className='api'><ApiComponent/></div>
      <img className='icon' src="https://images.vexels.com/media/users/3/234794/isolated/preview/b275da54cfbb602a136d3725090d4fd4-game-master-rpg-dice-badge.png" style={{ cursor: 'pointer' }} onClick={refreshPage} />
    </div>
  );
}

export default App;
