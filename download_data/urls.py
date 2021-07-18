from django.urls import path, include
from .views import export_project_answers_xls, export_project_user_answers_xls

app_name = 'download_data'

urlpatterns = [
    path('project/<int:id>/', export_project_answers_xls, name='download_response_data2'),
    path('project/<int:id>/<int:user>', export_project_user_answers_xls, name='download_response_data2')
]