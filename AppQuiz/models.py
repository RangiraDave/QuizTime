from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey


# Category model
class Category(models.Model):
    """
    Class to represent a category
    """
    name = CharField(max_length=100, unique=True)

    def __str__(self):
        """
        Returns the string representation of the category
        """
        return self.name

# Quiz model
class Quiz(models.Model):
    """
    Class to represent a quiz
    """
    LEVELS_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('advanced', 'Advanced'),
    ]

    title = CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=CASCADE, related_name='quizzes')
    level = models.CharField(max_length=10, choices=LEVELS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the quiz
        """
        return f"{self.title} - ({self.level})"


# Question model
class Question(models.Model):
    """
    Class to represent a question
    """
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
        )
    text = models.CharField(max_length=255)

    def __str__(self):
        """
        Returns the string representation of the question
        """
        return self.text


# Choice model
class Choice(models.Model):
    """
    Class to represent a choice
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
        )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns the string representation of the choice
        """
        return self.text


# Quiz result model
class QuizResult(models.Model):
    """
    Class to represent a quiz result
    """
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='quiz_results'
        )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=CASCADE,
        related_name='results'
        )
    score = IntegerField()
    completed_at = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        """
        Returns the string representation of the quiz result
        """
        return f"{self.user.username} - {self.quiz.title}: {self.score}"
