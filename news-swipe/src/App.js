// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NewsFeed from './components/NewsFeed'; // Assuming NewsFeed is a .js file, not .jsx

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* In React Router v6, you use "element" and pass the component wrapped in JSX */}
          <Route path="/" element={<NewsFeed />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
