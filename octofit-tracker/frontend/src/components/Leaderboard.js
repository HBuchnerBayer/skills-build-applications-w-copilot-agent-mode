import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboards/`;

function Leaderboard() {
  const [leaderboards, setLeaderboards] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Leaderboard API endpoint:', API_URL);
        console.log('Fetched leaderboards:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaderboards.map((entry, idx) => (
          <li className="list-group-item" key={idx}>
            Team: {entry.team} - Points: {entry.total_points}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
