from django.urls import path

from . import views

urlpatterns = [
    path("profile/", view=views.profile_view, name='profile')
]