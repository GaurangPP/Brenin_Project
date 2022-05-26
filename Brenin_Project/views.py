#To render HTML webpage

from distutils.log import info
from django.http import HttpResponse
from django.shortcuts import render
from info.forms import InputForm

from info.models import Info


def home_view(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        number = request.POST['number']
        query = request.POST['query']
        info = Info.objects.create(name=name, age=age, email=email, number=number, query=query)
        info.save()
        print(info.name)

    context = {}
    context['form'] = InputForm()
    

    return render(request, 'home.html', context)
