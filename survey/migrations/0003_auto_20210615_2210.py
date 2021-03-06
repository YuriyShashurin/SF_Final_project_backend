# Generated by Django 3.2 on 2021-06-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210614_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('multiple', 'Возможно несколько ответов'), ('single', 'Один ответ')], default='single', max_length=200),
        ),
        migrations.AlterField(
            model_name='respondentssurveystatusdata',
            name='answers',
            field=models.ManyToManyField(blank=True, null=True, through='survey.RespondentsAnswerData', to='survey.UsersAnswers'),
        ),
        migrations.AlterField(
            model_name='respondentssurveystatusdata',
            name='last_question',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='respondentssurveystatusdata',
            name='status',
            field=models.CharField(choices=[('Incomplete', 'Незавершенное интервью'), ('Not started', 'Не начато'), ('Complete', 'Завершенное интервью')], default='Not started', max_length=100),
        ),
        migrations.DeleteModel(
            name='RespondentsAnswerData2',
        ),
    ]
