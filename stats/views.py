from django.shortcuts import render
from survey.models import RespondentsSurveyStatusData
from django.http import JsonResponse

# Create your views here.


def compare_stats_score(request, project, current_stats):
    more_answers_score = 0
    arr = RespondentsSurveyStatusData.objects.filter(project=project, status='Complete')
    print(arr)
    for obj in arr:
        print(obj.answer_score)
        print(current_stats)
        if obj.answer_score < current_stats:
            more_answers_score += 1

    more_answers_score_persent = int(more_answers_score/len(arr))*100
    print(more_answers_score_persent)

    return JsonResponse({'more_answers_score_persent': more_answers_score_persent})



def compare_stats_time(request, project, current_stats):
    more_answers_time = 0
    arr = RespondentsSurveyStatusData.objects.filter(project=project, status='Complete')
    print(arr)
    for obj in arr:
        if obj.time < current_stats:
            more_answers_time += 1

    more_answers_time_persent = int(more_answers_time / len(arr)) * 100
    return JsonResponse({'more_answers_time_persent': more_answers_time_persent})