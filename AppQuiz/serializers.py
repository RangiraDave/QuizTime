from rest_framework import serializers
from .models import Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Quiz model
    """
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Question model
    """
    class Meta:
        model = Question
        fields = '__all__'
