from django.shortcuts import render
from .models import Project, AnswerOption, Survey, Question,RespondentsSurveyStatusData, RespondentsAnswerData, UsersAnswers
from .serializers import ProjectSerializer, AnswerSerializer, UserSerializer, QuestionSerializer, SurveySerializer, RespondentsAnswerDataSerializer, RespondentsSurveyStatusDataSerializer, UserAnswersSerializer
from rest_framework import permissions, viewsets, routers
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from survey.my_jwt_token import MyTokenObtainPairSerializer
from excel_response import ExcelResponse


# Create your views here.

class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RespondentsSurveyStatusDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RespondentsSurveyStatusData.objects.all()
    serializer_class = RespondentsSurveyStatusDataSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RespondentsAnswerDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RespondentsAnswerData.objects.all()
    serializer_class = RespondentsAnswerDataSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UsersAnswersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UsersAnswers.objects.all()
    serializer_class = UserAnswersSerializer
    # permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



def excelview(request):
    objs = RespondentsAnswerData.objects.all()
    return ExcelResponse(objs)