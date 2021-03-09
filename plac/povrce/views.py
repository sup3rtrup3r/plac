from django.views.generic import DetailView, ListView, CreateView

from .models import Povrce


class VegetableListView(ListView):
    model = Povrce


class VegetableDetailViev(DetailView):
    model = Povrce


class VegetableCreateView(CreateView):
    model = Povrce
    fields = ['name', 'description', 'vrsta', 'country_of_origin']
