from django.shortcuts import render

def home(request):

    data = {
        'title': 'Главная'
    }

    return render(request, 'app/home.html', data)

def service(request):
    return render(request, 'app/service.html', {'title': 'Сервис'})
