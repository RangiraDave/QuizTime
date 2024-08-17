# Applicatoin URL Configuration
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .admin import custom_admin_site
from .views import QuizViewSet, QuestionViewSet


# API URL Configuration
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # API URL
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
