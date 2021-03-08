from django.urls import path

from .views import VegetableListView


app_name = "povrce"
urlpatterns = [
    path(route='', view=VegetableListView.as_view(), name='list')
]
