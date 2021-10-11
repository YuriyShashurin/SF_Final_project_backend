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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        queryset = Project.objects.all()
        available = self.request.query_params.get('available')
        user_id = self.request.query_params.get('user_id')
        if available and user_id is not None:
            user_projects = RespondentsSurveyStatusData.objects.filter(user_id=user_id)

            available_projects = []
            for obj in user_projects:
                if obj.status != 'Complete':
                    available_projects.append(obj.project.id)

            queryset = Project.objects.filter(id__in=available_projects, is_active=True)

        return queryset


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def get_queryset(self):

        queryset = Survey.objects.all()
        question = self.request.query_params.get('question')
        project = self.request.query_params.get('project')
        if question and project is not None:
            queryset = queryset.filter(project=project, question=question)

        return queryset
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class RespondentsSurveyStatusDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RespondentsSurveyStatusData.objects.all()
    serializer_class = RespondentsSurveyStatusDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        queryset = RespondentsSurveyStatusData.objects.all()
        status = self.request.query_params.get('status')
        project = self.request.query_params.get('project')
        user_id = self.request.query_params.get('user_id')
        if status and project and user_id is not None:
            queryset = queryset.filter(project=project, question=status, user_id=user_id)
        elif (status and project is not None) and user_id is None:
            queryset = queryset.filter(project=project, status=status)
        elif (status and user_id is not None) and project is None:
            queryset = queryset.filter(status=status, user_id=user_id)

        return queryset


class RespondentsAnswerDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RespondentsAnswerData.objects.all()
    serializer_class = RespondentsAnswerDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersAnswersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UsersAnswers.objects.all()
    serializer_class = UserAnswersSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



def excelview(request):
    objs = RespondentsAnswerData.objects.all()
    return ExcelResponse(objs)