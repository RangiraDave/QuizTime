from django.contrib import admin
from .models import Quiz, Question, Category, Choice, QuizResult


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'category')
    list_filter = ['category', 'level']
    search_fields = ['title']


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score')
    list_filter = ['quiz']
    search_fields = ['user__username', 'quiz__title']


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
admin.site.register(Choice)

# Register your models here.
