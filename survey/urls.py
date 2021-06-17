from django.urls import path, include
from .views import ProjectsViewSet, SurveyViewSet, QuestionViewSet, AnswerViewSet, UserViewSet, RespondentsAnswerDataViewSet, RespondentsSurveyStatusDataViewSet, UsersAnswersViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
