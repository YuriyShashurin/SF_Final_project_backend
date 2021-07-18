import csv, xlwt

from django.http import HttpResponse
from survey.models import UsersAnswers, RespondentsSurveyStatusData


def export_project_answers_xls(request, id):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="project_{}.xls"'.format(id)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('project_{}'.format(id))

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['project', 'user', 'question', 'ValueofAnswer', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = RespondentsSurveyStatusData.objects.filter(project=1, status='Complete').values_list('answers__project__title', 'user_id__username', 'answers__question__title', 'respondentsanswerdata__user_answers__answer')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_project_user_answers_xls(request, id, user):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="project_{}_user_{}.xls"'.format(id, user)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('project_{}_user_{}'.format(id, user))

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['project', 'user', 'question', 'ValueofAnswer', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = RespondentsSurveyStatusData.objects.filter(project=1, status='Complete', user_id=user).values_list('answers__project__title', 'user_id__username', 'answers__question__title', 'respondentsanswerdata__user_answers__answer')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response