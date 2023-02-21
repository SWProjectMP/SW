from django.urls import path

from . import views

urlpatterns = [
    path('search/', view=views.index, name='search'),
]