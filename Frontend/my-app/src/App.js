import React from 'react';

// styling
import './App.css';

// components 
import Container from './components/Container';
import Home from './components/Home';
import SignUp from './components/SignUp';
import { Switch, Route } from 'react-router-dom';
const App = () => {
  return (
    <Switch>
      <Route path='/home'>
        <Home />
      </Route>
      <Route path='/'>
        <div className="App cfb">
          <Container />
        </div>

      </Route>
    </Switch>
    // <div className="App cfb">
    //   <Container />
    // </div>
  );
}

export default App;