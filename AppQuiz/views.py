# Authentication views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import QuizResult, Quiz, Question, Choice, Category


# Home view implementation
@login_required
def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    return render(request, 'home.html')


# User registration view implementation
def signup_view(request):
    """
    View function for handling user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# User login view implementation
def login_view(request):
    """
    View function for handling user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None

    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, 'Logged in successfully')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# User logout view implementation
@login_required
def logout_view(request):
    """
    View function for handling user logout.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('login')


# profile view implementation
@login_required
def profile_view(request):
    """
    View function for the user profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    user = request.user
    quiz_results = QuizResult.objects.filter(user=user)

    # Calculate total score
    total_score = sum(result.score for result in quiz_results)

    # Fetch the user's worldwide ranking
    worldwide_rank = QuizResult.objects.filter(score__gt=total_score).count() + 1

    # Get distinct categories the user has taken quizzes in
    categories_taken = set(result.quiz.category for result in quiz_results)

    # Calculate scores by category
    scores_by_category = {category: 0 for category in categories_taken}
    for result in quiz_results:
        scores_by_category[result.quiz.category] += result.score

    context = {
        'username': user.username,
        'quiz_results': quiz_results,
        'total_score': total_score,
        'worldwide_rank': worldwide_rank,
        'scores_by_category': scores_by_category
    }

    return render(request, 'profile.html', context)


# Category list view implementation
def category_list(request):
    """
    View function for the category list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object
    """
    categories = Category.objects.all()
    return render(
        request,
        'category_list.html',
        {'categories': categories}
        )


# Quiz list view implementation
def quiz_list(request, category_id):
    """
    View function for the quiz list page.
    It will list all quizzes in a given category and level.

    Args:
        request (HttpRequest): The HTTP request object.
        category_id (int): The
        category ID.

    Returns:
        HttpResponse: The HTTP response object.
    """
    category = get_object_or_404(Category, id=category_id)
    quizzes = Quiz.objects.filter(category=category)
    return render(
        request,
        'quiz_list.html',
        {'category': category,
        'quizzes': quizzes}
        )


# Take quiz view implementation
@login_required
def take_quiz(request, quiz_id):
    """
    View function for taking a quiz.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_id (int): The quiz ID.

    Returns:
        HttpResponse: The HTTP response object.
    """
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user = request.user
    questions = quiz.questions.all()

    # Check if the user has already taken this quiz
    existing_result = QuizResult.objects.filter(user=user, quiz=quiz).first()
    if QuizResult.objects.filter(user=user, quiz=quiz).exists():
        messages.warning(request, 'You have already taken this quiz.')
        return redirect('quiz_result', quiz_id=quiz.id, score=existing_result.score)

    if request.method == 'POST':
        score = 0
        unanswered_questions = False

        for question in questions:
            selected_choice = request.POST.get(f'question_{question.id}')
            if not selected_choice:
                unanswered_questions = True
                break
            else:
                selected_choice = Choice.objects.get(id=selected_choice)
                if selected_choice.is_correct:
                    score += 1

        # If there are unanswered questions, show an error message
        if unanswered_questions:
            messages.error(request, 'Please answer all questions before submitting the quiz.')
            return render(request, 'take_quiz.html', {'quiz': quiz, 'questions': questions})

        QuizResult.objects.create(user=user, quiz=quiz, score=score)
        return redirect('quiz_result', quiz_id=quiz.id, score=score)

    return render(request, 'take_quiz.html', {'quiz': quiz, 'questions': questions})


# Quiz result view implementation
@login_required
def quiz_result(request, quiz_id, score=None):
    """
    View function for displaying the quiz result.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_id (int): The quiz ID.
        score (int): The user's score.

    Returns:
        HttpResponse: The HTTP response object.
    """
    quiz = get_object_or_404(Quiz, id=quiz_id)
    category_id = quiz.category.id
    questions = quiz.questions.all()
    total_questions = questions.count()
    user = request.user
    percentage = (score / questions.count()) * 100 if total_questions > 0 else 0

    # If the score is not provided, it means the user is not supposed to see the result
    if score is None:
        result = QuizResult.objects.filter(user=user, quiz=quiz).first()
        if result:
            score = result.score
        else:
            messages.error(request, 'You have not taken this quiz yet.')
            return redirect('home')

    category_id = quiz.category.id
    return render(
        request,
        'quiz_result.html',
        {
            'quiz': quiz,
            'score': score,
            'category_id': category_id,
            'percentage': percentage,
            'questions': questions
            }
    )
