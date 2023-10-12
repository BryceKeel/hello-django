// main.js

// Function to fetch a random D&D 5E monster
async function getRandomMonster() {
    try {
      const response = await fetch('https://www.dnd5eapi.co/api/monsters');
      const data = await response.json();
      
      // Get a random monster from the list
      const randomIndex = Math.floor(Math.random() * data.count);
      const randomMonsterUrl = data.results[randomIndex].url;
  
      // Fetch the details of the random monster
      const monsterResponse = await fetch(`https://www.dnd5eapi.co${randomMonsterUrl}`);
      const monsterData = await monsterResponse.json();
  
      // Extract the relevant monster information
      const monsterName = monsterData.name;
      const monsterType = monsterData.type;
      const monsterChallengeRating = monsterData.challenge_rating;
      const monsterAlignment = monsterData.alignment;
  
      // Create a string to display the monster information
      const monsterInfo = `Name: ${monsterName}\nType: ${monsterType}\nChallenge Rating: ${monsterChallengeRating}\nAlignment: ${monsterAlignment}`;
  
      // Display the monster information on the webpage
      document.getElementById('monster-info').textContent = monsterInfo;
    } catch (error) {
      console.error('Error fetching random monster:', error);
    }
  }
  
  // Add an event listener to a button that triggers the getRandomMonster function
  document.getElementById('random-monster-button').addEventListener('click', getRandomMonster);
  