from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        "title": "Главная страница",
        "values": ['Some', 'Test', 'Text'],
        'obj': {
            'car': 'Mersedes',
            'age': 25,
            'hobby': 'Game'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
