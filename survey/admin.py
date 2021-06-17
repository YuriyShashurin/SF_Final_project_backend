from django.contrib import admin
from .models import Survey, Question, AnswerOption,Project, RespondentsSurveyStatusData, RespondentsAnswerData, UsersAnswers

# Register your models here.


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(RespondentsSurveyStatusData)
class RespondentsSurveyStatusDataAdmin(admin.ModelAdmin):
    fields = ['project', 'user_id', 'status']


@admin.register(RespondentsAnswerData)
class RespondentsAnswerDataAdmin(admin.ModelAdmin):
    pass


@admin.register(UsersAnswers)
class RespondentsAnswerDataAdmin(admin.ModelAdmin):
    fields = ['project', 'user_id', 'question', 'answer']