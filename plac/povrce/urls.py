from django.urls import path

from .views import VegetableListView, VegetableDetailViev


app_name = "povrce"
urlpatterns = [
    path(route='', view=VegetableListView.as_view(), name='list'),
    path(route='<slug:slug>', view=VegetableDetailViev.as_view(), name='detail')
]
