from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


# Create your models here.

class AnswerOption(models.Model):
    text = models.CharField(max_length=200)
    value = models.SmallIntegerField()

    def __str__(self):
        return self.text


class Question(models.Model):
    SINGLE = 'single'
    MUlTIPLE = 'multiple'

    TYPE_CHOICES = {
        (SINGLE, 'Один ответ'),
        (MUlTIPLE, 'Возможно несколько ответов'),
    }

    title = models.CharField(max_length=100)
    help_desc = models.CharField(max_length=200, default='', blank=True, )
    type = models.CharField(choices=TYPE_CHOICES, default=SINGLE, max_length=200)
    answer_option = models.ManyToManyField(AnswerOption)

    def __str__(self):
        return self.title


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publication_date = models.DateField(default=timezone.now)
    closing_date = models.DateField(default=timezone.now)
    life_time_value = models.IntegerField(default=60)
    is_active = models.BooleanField(default=False)
    question = models.ManyToManyField(Question, through='Survey')
    complete_code = models.UUIDField(verbose_name='Код завершенного интервью', default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title


class Survey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    weight = models.SmallIntegerField()


class UsersAnswers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.PositiveSmallIntegerField()


class RespondentsSurveyStatusData(models.Model):
    COMPLETE = 'Complete'
    INCOMPLETE = 'Incomplete'
    NOT_STARTED = 'Not started'

    STATUS_CHOICES = {
        (COMPLETE, 'Завершенное интервью'),
        (INCOMPLETE, 'Незавершенное интервью'),
        (NOT_STARTED, 'Не начато'),
    }

    id = models.CharField(max_length=11, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='Проект')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    status = models.CharField(choices=STATUS_CHOICES, default=NOT_STARTED, max_length=100)
    last_question = models.SmallIntegerField(default=0, blank=True)
    answers = models.ManyToManyField(UsersAnswers, through='RespondentsAnswerData', blank=True)

    def save(self, *args, **kwargs):
        self.id = '{}_{}'.format(self.project.id, self.user_id.id)
        super(RespondentsSurveyStatusData, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_id.username


class RespondentsAnswerData(models.Model):
    survey_status = models.ForeignKey(RespondentsSurveyStatusData, on_delete=models.CASCADE)
    user_answers = models.ForeignKey(UsersAnswers, on_delete=models.CASCADE)

