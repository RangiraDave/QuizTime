import React from 'react';
import './App.css';
import QuizList from './components/QuizList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>QuizTime</h1>
      </header>
      <QuizList />
    </div>
  );
}

export default App;
