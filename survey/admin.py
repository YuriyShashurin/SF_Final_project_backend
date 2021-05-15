from django.contrib import admin
from .models import Survey, Question, AnswerOption,Project

# Register your models here.
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(AnswerOption)
class Answer_OptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class Project_OptionAdmin(admin.ModelAdmin):
    pass