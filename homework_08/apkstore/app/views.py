from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import AppCreateForm
from .models import App


def index(request):
    all_apps = App.objects.prefetch_related().all()
    context = {
        'all_apps': all_apps
    }
    return render(request, 'app/index.html', context=context)


class AppDetailView(DetailView):
    model = App
    page_title = 'App Name'


class AppListView(ListView):
    model = App
    paginate_by = 4


class AppCreateView(CreateView):
    model = App
    success_url = reverse_lazy('main')
    form_class = AppCreateForm
    # fields = '__all__'
