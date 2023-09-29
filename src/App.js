import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [currentLocation, setCurrentLocation] = useState('');

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude } = position.coords;
        fetch(`/weather?lat=${latitude}&lng=${longitude}`)
          .then(res => res.json())
          .then(data => {
            setCurrentLocation(data.location);
          });
      });
    }

    return () => clearInterval(interval); // Clean up the interval on component unmount
  }, []);

  const options = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  const formattedTime = currentTime.toLocaleTimeString('en-US', options);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>Current time is {formattedTime}.</p>
        <p>Your current location is {currentLocation}.</p>
      </header>
    </div>
  );
}

export default App;
