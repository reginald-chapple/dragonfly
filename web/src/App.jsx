import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Replace with your actual Django API endpoint
        const response = await fetch('http://127.0.0.1:8000/api/test/');
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>React (with Vite) and Django Integration</h1>
        {data ? (
          <div>
            <h2>Data from Django:</h2>
            <pre>{JSON.stringify(data.message, null, 2)}</pre>
          </div>
        ) : (
          <p>Loading data from Django...</p>
        )}
      </header>
    </div>
  );
}

export default App;