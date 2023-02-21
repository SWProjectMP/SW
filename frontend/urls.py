from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.home_view, name='home'),
    path('projects/', view=views.project_view),
    path('project/<str:project_id>', view=views.project)
]