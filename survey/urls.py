from django.urls import path, include
from .views import ProjectsViewSet, SurveyViewSet, QuestionViewSet, AnswerViewSet, UserViewSet, RespondentsAnswerDataViewSet, RespondentsSurveyStatusDataViewSet, UsersAnswersViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

app_name = 'survey'

router = DefaultRouter()
router.register('projects', ProjectsViewSet)
router.register('surveys', SurveyViewSet)
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('users', UserViewSet)
router.register('project_status', RespondentsSurveyStatusDataViewSet)
router.register('answers_in_project', RespondentsAnswerDataViewSet)
router.register('users_answers', UsersAnswersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="SurveysHR",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
