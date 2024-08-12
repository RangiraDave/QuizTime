# Applicatoin URL Configuration
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz'),
    # path('result/<int:quiz_id>/', views.result_view, name='result'),
]
