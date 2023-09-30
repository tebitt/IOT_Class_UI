import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [currentTemp, setTemp] = useState(0);
  const [currentFeels, setFeels] = useState(0);
  const [currentRain, setRain] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude } = position.coords;
        fetch(`/temp?lat=${latitude}&lng=${longitude}`)
          .then(res => res.json())
          .then(data => {
            setTemp(data.temp);
            setFeels(data.feels);
          });
        fetch(`/rain?lat=${latitude}&lng=${longitude}`)
          .then(res => res.json())
          .then(data => {
            setRain(data.percip);
          });
        });
      }
    }, 5000); // need to change to 1 hour in the real app 
    return () => clearInterval(interval);
  }, []);

  const options = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  const formattedTime = currentTime.toLocaleTimeString('en-US', options);

  return (
    <div className="App">
      <header className="App-header">
        <div className="app-container">
          <div className="block left-block">
            <div className="info">
              <p>Current time is {formattedTime}.</p>
              <p>Current temp is {currentTemp} and feels like {currentFeels}.</p>
              <p>Percipitation percentage is {currentRain}%.</p>
            </div>
            <div className="icons">
              {/* Add icons here */}
            </div>
          </div>
          <div className="block right-block">
            <div className="section bus">
              <h2>Bus</h2>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
            </div>
            <div className="section destination">
              <h2>Destination</h2>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
            </div>
            <div className="section arrival">
              <h2>Arrival</h2>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
              <div className="box"></div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;