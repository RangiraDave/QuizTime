from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ValidationError
# from .models import Quiz, Question, Answer, Result
from .models import Question
from tinymce.widgets import TinyMCE


# User registration form
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'confirm_password'
            ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class QuestionAdminForm(forms.ModelForm):
    """
    Form for the Question model in the admin
    """
    # Use TinyMCE widget for text field
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        choices = cleaned_data.get('choices')
        correct_choices = [choice for choice in choices if choice.is_correct]
        if not correct_choices:
            raise ValidationError('At least one choice must be correct')
        return cleaned_data


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Custom admin for Question model
    """
    form = QuestionAdminForm
