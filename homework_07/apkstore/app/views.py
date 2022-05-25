from django.shortcuts import render

from .models import App


def index(request):
    all_apps = App.objects.prefetch_related().all()
    context = {
        'all_apps': all_apps
    }
    return render(request, 'index.html', context=context)
