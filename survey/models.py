from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class AdminUser(User):

    EMPLOYER = 'employer'
    HR = 'HR'

    USER_STATUS = {
        (EMPLOYER, 'Сотрудник'),
        (HR, 'HR-специалист'),
    }
    is_admin = models.CharField(choices=USER_STATUS, default=EMPLOYER, max_length=100)

    def __str__(self):
        return self.is_admin


class AnswerOption(models.Model):
    text = models.CharField(max_length=200)
    value = models.SmallIntegerField()

    def __str__(self):
        return self.text


class Question(models.Model):
    SINGLE = 'single'
    MUlTIPLE = 'multiple'

    TYPE_CHOICES = {
        (SINGLE, 'single'),
        (MUlTIPLE, 'multiple'),
    }

    title = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_CHOICES,default=SINGLE, max_length=200)
    answer_option = models.ManyToManyField(AnswerOption)

    def __str__(self):
        return self.title


class Project (models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publication_date = models.DateField(default=timezone.now)
    closing_date = models.DateField(default=timezone.now)
    life_time_value = models.IntegerField(default=60)
    is_active = models.BooleanField(default=False)
    question = models.ManyToManyField(Question, through='Survey')

    def __str__(self):
        return self.title


class Survey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    weight = models.SmallIntegerField()

    def __str__(self):
        return self.project


class RespondentData(models.Model):
    pass