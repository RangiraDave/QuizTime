# Applicatoin URL Configuration
from django.urls import path
from . import views
from .admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # Custom admin site
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='categories'),
    path('quizzes/<int:category_id>/', views.quiz_list, name='quiz_list'),
    path('quiz_result/<int:quiz_id>/<int:score>/', views.quiz_result, name='quiz_result'),
    path('take_quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
]
