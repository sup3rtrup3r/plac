from django.views.generic import DetailView, ListView

from .models import Povrce


class VegetableListView(ListView):
    model = Povrce


class VegetableDetailViev(DetailView):
    model = Povrce
