import React, { useState, useEffect } from 'react';

function ApiComponent() {
  const [data, setData] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [characterName, setCharacterName] = useState('');
  const [initiativeBonus, setInitiativeBonus] = useState(0);
  const [initiativeList, setInitiativeList] = useState([]);
  const [currentTurn, setCurrentTurn] = useState(0);
  const [diceResult, setDiceResult] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(`https://www.dnd5eapi.co/api/${searchQuery}`);
      if (response.ok) {
        const result = await response.json();
        setData(result);
      } else {
        console.error('Failed to fetch data from the API');
        setData(null);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }

    setIsLoading(false);
  };

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearch = (event) => {
    event.preventDefault(); // Prevent form submission
    fetchData();
  };

  const addCharacterToInitiative = () => {
    const totalInitiative = rollInitiative();
    const updatedInitiativeList = [...initiativeList, { characterName, totalInitiative }];
    updatedInitiativeList.sort((a, b) => b.totalInitiative - a.totalInitiative);
    setInitiativeList(updatedInitiativeList);
    setCharacterName('');
    setInitiativeBonus(0);
  };

  const rollInitiative = () => {
    return Math.floor(Math.random() * 20) + 1 + initiativeBonus;
  };

  const rollDice = (sides) => {
    const result = Math.floor(Math.random() * sides) + 1;
    setDiceResult(result);
  };

  const rollD100 = () => {
    const result = Math.floor(Math.random() * 100) + 1;
    setDiceResult(result);
  };

  const nextTurn = () => {
    setCurrentTurn((currentTurn + 1) % initiativeList.length);
  };

  const handleInitiativeKeyPress = (event) => {
    if (event.key === 'Enter') {
      addCharacterToInitiative();
    }
  };

  return (
    <div>
      <div>
        <h2>Dice Roller</h2>
        <button className='button' onClick={() => rollDice(4)}>Roll D4</button>
        <button className='button' onClick={() => rollDice(6)}>Roll D6</button>
        <button className='button' onClick={() => rollDice(8)}>Roll D8</button>
        <button className='button' onClick={() => rollDice(10)}>Roll D10</button>
        <button className='button' onClick={() => rollDice(12)}>Roll D12</button>
        <button className='button' onClick={() => rollDice(20)}>Roll D20</button>
        <button className='button' onClick={rollD100}>Roll D100</button>
        {diceResult && <p>Result: {diceResult}</p>}
      </div>
      <div>
        <h2>Initiative Tracker</h2>
        <input
          type="text"
          placeholder="Character Name"
          value={characterName}
          onChange={(e) => setCharacterName(e.target.value)}
          onKeyPress={handleInitiativeKeyPress}
        />
        <input
          type="number"
          placeholder="Initiative Bonus"
          value={initiativeBonus}
          onChange={(e) => setInitiativeBonus(parseInt(e.target.value, 10) || 0)}
          onKeyPress={handleInitiativeKeyPress}
        />
        <button
          className='button'
          onClick={addCharacterToInitiative}
          disabled={!characterName}
        >
          Add to Initiative
        </button>
        <button className='button' onClick={nextTurn}>Next Turn</button>
        <ul>
          {initiativeList.map((item, index) => (
            <li key={index}>
              {item.characterName}: {item.totalInitiative}
              {index === currentTurn && ' (Current Turn)'}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Search Bar</h2>
        <form onSubmit={handleSearch}>
          <input
            className='searchbar'
            type="text"
            placeholder="Search D&D 5e API"
            value={searchQuery}
            onChange={handleSearchChange}
          />
          <button className='button' type="submit">Search</button>
        </form>
      </div>
      {isLoading ? (
        <p>Loading data...</p>
      ) : data ? (
        <div>
          <h1>API Data</h1>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      ) : (
        <p>No data available. Try searching for a valid resource.</p>
      )}
    </div>
  );
}

export default ApiComponent;
