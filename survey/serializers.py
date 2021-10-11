from rest_framework import serializers
from .models import Project, Survey, AnswerOption, Question, RespondentsAnswerData, RespondentsSurveyStatusData, \
    UsersAnswers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'first_name', 'last_name', 'is_staff', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=AnswerOption._meta.get_field('id'), required=False)

    class Meta:
        model = AnswerOption
        fields = ['id', 'text', 'value']


class SurveySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Survey._meta.get_field('id'), required=False)

    class Meta:
        model = Survey
        fields = ['id', 'project', 'question', 'weight']


class QuestionSerializer(serializers.ModelSerializer):
    answer_option = AnswerSerializer(many=True)
    type_display = serializers.CharField(source='get_type_display', required=False, allow_blank=True,read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'type', 'help_desc', 'answer_option', 'type_display']

    def create(self, validated_data):
        answer_option = validated_data.pop('answer_option', None)
        new_instance = Question.objects.create(**validated_data)
        for option in answer_option:
            opt = dict(option)
            opt = AnswerOption.objects.get(pk=opt['id'])
            new_instance.answer_option.add(opt)
        new_instance.save()
        return new_instance


class ProjectSerializer(serializers.ModelSerializer):
    owner_id = serializers.CharField()
    owner = UserSerializer(required=False, read_only=True)
    question = QuestionSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'owner', 'owner_id', 'title', 'description', 'complete_code', 'publication_date', 'closing_date',
                  'life_time_value', 'is_active', 'question']

    def create(self, validated_data):
        owner_id = validated_data.pop('owner_id', None)
        new_instance = Project.objects.create(**validated_data)
        owner = User.objects.filter(pk=int(owner_id))[0]
        new_instance.owner = owner
        new_instance.save()
        return new_instance


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswers
        fields = '__all__'


class RespondentsSurveyStatusDataSerializer(serializers.ModelSerializer):
    answers = UserAnswersSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = RespondentsSurveyStatusData
        fields = ['id', 'project', 'user_id', 'status', 'last_question', 'answers', 'project_score', 'answer_score', 'time','remaining_time']


class RespondentsAnswerDataSerializer(serializers.ModelSerializer):
    user_answers = UserAnswersSerializer()

    class Meta:
        model = RespondentsAnswerData
        fields = ['id', 'survey_status', 'user_answers']

    def create(self, validated_data):
        st = validated_data.pop('survey_status')
        st2 = dict(validated_data.pop('user_answers'))
        answer = st2.pop('answer')
        project = st2.pop('project')
        user_id = st2.pop('user_id')
        question = st2.pop('question')
        survey_status = RespondentsSurveyStatusData.objects.get(id=st.id)
        user_answers = UsersAnswers.objects.create(project=project,answer=answer,question=question,user_id=user_id)
        instance = RespondentsAnswerData.objects.create(survey_status=survey_status, user_answers=user_answers)
        return instance
