import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NewsFeed from './components/NewsFeed';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={NewsFeed} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
