from rest_framework import serializers
from .models import Project, Survey, AnswerOption, Question
from django.contrib.auth.models import User


class UserSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name','email', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = ['id','owner', 'title', 'description', 'publication_date', 'closing_date', 'life_time_value', 'is_active', 'question']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta():
        model = AnswerOption
        fields = ['id','text', 'value']


class SurveySerializer(serializers.ModelSerializer):
    class Meta():
        model = Survey
        fields = ['id','project', 'question', 'weight']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Question
        fields = ['id','title', 'type', 'answer_option']