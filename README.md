# QuizTime

QuizTime is a web-based interactive quiz application built with Django. The application allows users to register, take quizzes, and review their results. It features a custom admin dashboard, a dynamic quiz-taking interface, and supports a variety of question types.

## Features

- **User Authentication**: Users can register, log in, and manage their accounts.
- **Quizzes**: Create and manage quizzes with categories, levels, and time limits.
- **Questions and Choices**: Add multiple-choice questions with options, and mark the correct answer.
- **Admin Dashboard**: A custom admin interface to manage quizzes, categories, questions, and more.
- **Progress Tracking**: Track quiz progress with a dynamic progress bar.
- **Timer**: Each quiz has a time limit, which is displayed to the user during the quiz.
- **Responsive Design**: Built with Bootstrap to ensure a responsive and user-friendly interface.

## Project Structure

- **models.py**: Defines the database models for categories, quizzes, questions, and choices.
- **forms.py**: Contains forms for user registration and question/choice management in the admin.
- **views.py**: Handles the logic for rendering quizzes, processing user input, and displaying results.
- **urls.py**: Defines the URL patterns for the app.
- **admin.py**: Customizes the Django admin interface to manage quizzes and questions.
- **templates/**: Contains the HTML templates for the application, including base templates and specific pages like the quiz-taking interface.
- **static/**: Includes static files like CSS and JavaScript for the front end.
- **requirements.txt**: Lists the dependencies required to run the application.

## Installation

To get started with the QuizTime project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Django
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/QuizTime.git
cd QuizTime
```

### Step 2: Create and Activate a Virtual Environment
```bash
python3 -m venv qvenv
source qvenv/bin/activate  # On Windows, use `qvenv\Scripts\activate`
```

### Step 3: Install the Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations
```bash
python3 manage.py migrate
```

### Step 5: Create a SuperUser
```bash
python3 manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python3 manage.py runserver
```

You can now access the application at `http://127.0.0.0.1:8000/`.


## Deployment
QuizTime is deployed to PythonAnywhere platform.
For more detailed deployment instructions, refer to the [PythonAnywhere documentation](https://help.pythonanywhere.com/)


## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.


## Contribution
Contributions are welcome! Please fork this repository and submit a pull request with your changes.


## Contact
For questions or support, please reach out to [Rangira](https://mail.google.com/mail/u/0/#inbox?compose=hlSwpfPgjgRgxcXXNNqXrMxDPGkhZGMPnMBnTzwGLbVfJCTkWzxBTJGLNmlFwrtnnFKzHDcFZlVNjZRlhmHsjFCMftdbQdmrLrplLNNVhCLcBkslqSQkkvcWvGxDQ)


## HappyCoding!
