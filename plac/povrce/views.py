from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Povrce


class VegetableListView(ListView):
    model = Povrce


class VegetableDetailViev(DetailView):
    model = Povrce


class VegetableCreateView(LoginRequiredMixin, CreateView):
    model = Povrce
    fields = ['name', 'description', 'vrsta', 'country_of_origin']
