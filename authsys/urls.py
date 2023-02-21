from django.urls import path

from . import views

urlpatterns = [
    path('register/', view=views.register_view, name='register'),
    path('login/', view=views.login_view, name='login'),
    path('email_verify/', view=views.verify_email)
]