import React, { useState, useEffect } from 'react';
import axios from 'axios';

const QuizList = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/quizzes/')
      .then(response => {
        console.log('API response:', response.data); // Log the response data
        setQuizzes(response.data);
      })
      .catch(error => {
        console.error('There was an error while fetching quizzes!', error);
        setError(`There was an error while fetching quizzes! ${error.message}`);
      });
  }, []);

  return (
    <div>
      <h1>Quiz List</h1>
      {error && <p>{error}</p>}
      <ul>
        {quizzes.map(quiz => (
          <li key={quiz.id}>{quiz.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default QuizList;
