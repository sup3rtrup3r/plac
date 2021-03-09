from django.urls import path

from .views import VegetableListView, VegetableDetailViev, VegetableCreateView


app_name = "povrce"
urlpatterns = [
    path(route='', view=VegetableListView.as_view(), name='list'),
    path(route='add/', view=VegetableCreateView.as_view(), name='create'),
    path(route='<slug:slug>/', view=VegetableDetailViev.as_view(), name='detail'),
]
