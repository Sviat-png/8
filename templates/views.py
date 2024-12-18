from django.shortcuts import render
from .models import Locomotive, Repair, `, Worker

def project_info(request):
    Cinema = Cinema.objects.all()
    Movie = Movie.objects.all()
    Screening = Screening.objects.all()

    return render(request, 'project_info.html', {
        'project_name': 'Лабораторна робота №8',  
        'student_name': 'Прокопенко Святослав Юрійович',
        'student_group': 'КБ21015Б',
        'Locomotive': Locomotive,
        'Repair': Repair,
        'Worker': Worker,
    })
