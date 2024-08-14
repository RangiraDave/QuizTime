from django.urls import path
from django.contrib import admin
from .models import Category, Quiz, Question, Choice
from django.shortcuts import render
from django.utils.html import format_html


# Inline models
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Custom admin for Quiz model
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'time_limit', 'created_at')
    list_filter = ('category', 'level', 'created_at')
    search_fields = ('title', 'category__name')
    inlines = [QuestionInline]
    actions = ['duplicate_quiz']

    def duplicate_quiz(self, request, queryset):
        for quiz in queryset:
            quiz.pk = None
            quiz.title = f"{quiz.title} (Copy)"
            quiz.save()
    duplicate_quiz.short_description = "Duplicate selected quizzes"


# Custom admin for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Custom admin for Question model
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'quiz')
#     search_fields = ('text', 'quiz__title')
#     inlines = [ChoiceInline]


# Custom admin dashboard view
def custom_admin_dashboard(request):
    context = {
        'quizzes_count': Quiz.objects.count(),
        'categories_count': Category.objects.count(),
        'questions_count': Question.objects.count(),
        'choices_count': Choice.objects.count(),
    }
    return render(request, 'admin/custom_dashboard.html', context)


# Adding the custom dashboard to the admin site
class CustomAdminSite(admin.AdminSite):
    site_header = 'My custom admin dashboard'
    site_title = 'Admin portal'
    index_title = 'Welcome to the admin portal'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(custom_admin_dashboard), name='custom_dashboard'),
        ]
        return custom_urls + urls


# Register the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(Category, CategoryAdmin)
custom_admin_site.register(Quiz, QuizAdmin)
# custom_admin_site.register(Question, QuestionInline)
custom_admin_site.register(Choice)
