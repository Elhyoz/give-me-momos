from django.shortcuts import render

from blog.models import Momo


def index(request):
    template = 'index.html'
    context = {
        'pregunta': 'kiere magia prro?',
        'magia': 'toma tus momos :V'
    }

    return render(request, template, context)


def momos(request):
    los_momos = Momo.objects.all()
    template = 'momos/momos.html'
    context = {
        'momos': los_momos,
    }

    return render(request, template, context)


def new_momo(request):
    los_momos = Momo.objects.all()
    template = 'momos/momos.html'
    context = {
        'momos': los_momos,
    }

    return render(request, template, context)