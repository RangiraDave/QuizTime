"""
This file contains the admin configuration for the Quiz app.
"""
from django.urls import path
from django.contrib import admin
from .models import Category, Quiz, Question, Choice
from django.shortcuts import render
from django.utils.html import format_html
from .models import Question


# Inline models
class QuestionInline(admin.TabularInline):
    """
    Inline model for the Question model
    """
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    """
    Inline model for the Choice model
    """
    model = Choice
    extra = 4


# Custom admin for Quiz model
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Quiz model
    """
    list_display = ('title', 'category', 'level', 'time_limit', 'created_at')
    list_filter = ('category', 'level', 'created_at')
    search_fields = ('title', 'category__name')
    inlines = [QuestionInline]
    actions = ['duplicate_quiz']

    def duplicate_quiz(self, request, queryset):
        """
        Method to duplicate selected quizzes

        Args:
            request (HttpRequest): The HTTP request object
            queryset (QuerySet): The selected quizzes

        Returns:
            None
        """
        for quiz in queryset:
            quiz.pk = None
            quiz.title = f"{quiz.title} (Copy)"
            quiz.save()
    duplicate_quiz.short_description = "Duplicate selected quizzes"


# Custom admin for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Category model
    """
    list_display = ('name',)
    search_fields = ('name',)


# Custom admin for Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Question model
    """
    list_display = ('text', 'quiz')
    search_fields = ('text', 'quiz__title')
    inlines = [ChoiceInline]


# Custom admin dashboard view
def custom_admin_dashboard(request):
    """
    Custom admin dashboard view

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response object
    """
    context = {
        'quizzes_count': Quiz.objects.count(),
        'categories_count': Category.objects.count(),
        'questions_count': Question.objects.count(),
        'choices_count': Choice.objects.count(),
    }
    return render(request, 'admin/custom_dashboard.html', context)


# Adding the custom dashboard to the admin site
class CustomAdminSite(admin.AdminSite):
    """
    Custom admin site class
    """
    site_header = 'My custom admin dashboard'
    site_title = 'Admin portal'
    index_title = 'Welcome to the admin portal'

    def get_urls(self):
        """
        Method to get the custom URLs

        Returns:
            list: The list of custom URLs
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                'dashboard/',
                self.admin_view(custom_admin_dashboard),
                name='custom_dashboard'
                ),
        ]
        return custom_urls + urls


# Register the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(Category, CategoryAdmin)
custom_admin_site.register(Quiz, QuizAdmin)
custom_admin_site.register(Choice)
custom_admin_site.register(Question, QuestionAdmin)
