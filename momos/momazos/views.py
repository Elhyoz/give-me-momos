from django.shortcuts import render
from django.http import HttpResponse

from .models import Momo

def index(request):
    template = 'index.html'
    context = {
        'pregunta': 'kiere magia prro?',
        'magia': 'toma tus momos :V'
    }

    return render(request, template, context)


def momos(request):
    los_momos = Momo.objects.all()
    template = 'momos.html'
    context = {
        'momos': los_momos,
    }

    return render(request, template, context)