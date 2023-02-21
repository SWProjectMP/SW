from django.contrib.auth import login, authenticate
from django.core.handlers.wsgi import WSGIRequest

from api.models import Profile


import uuid

def is_authentication_success(request: WSGIRequest) -> bool:
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    if not user:
        return True
    else:
        login(request, user)
    return False

def register_user(request: WSGIRequest) -> None:
    Profile.objects.create_user(
        username=request.POST["username"],
        password=request.POST["password"],
        email=request.POST["email"],
        profile_id=str(uuid.uuid4())
    )
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    login(request, user)
