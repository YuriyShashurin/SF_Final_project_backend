from django.urls import path
from .views import compare_stats_score, compare_stats_time


app_name = 'stats'

urlpatterns = [
    path('score_stats/<int:project>/<int:current_stats>', compare_stats_score, name='compare_stats_score'),
    path('time_stats/<int:project>/<int:current_stats>', compare_stats_time, name='compare_stats_time')
]