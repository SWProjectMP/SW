from django.urls import path

from api.views import auth
from api.views import projects

urlpatterns = [
    path('register/', view=auth.register_handler, name='api_auth_register'),
    path('login/', view=auth.login_handler, name='api_auth_login'),
    path('logout/', view=auth.logout_hanlder, name='api_auth_logout'),
    path('email_verify/<str:profile_id>/<str:auth_key>/', view=auth.verify_email_user),

    path('get_projects/', view=projects.get_projects),

]