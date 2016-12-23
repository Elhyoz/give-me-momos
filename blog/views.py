from django.shortcuts import render, redirect

from blog.forms import MomoForm
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
    if request.method == 'POST':
        form = MomoForm(request.POST, request.FILES)
        if form.is_valid():
            momo = form.save(commit=False)
            momo.save()
            return redirect('/momos/')
    else:
        form = MomoForm()

    momo_objects = Momo.objects.all()
    template = 'momos/new_momo.html'
    context = {
        'momos': momo_objects,
        'form': form
    }

    return render(request, template, context)