from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


from api.models import Profile, ProfilesToVerify
from api.auth import is_authentication_success, register_user
from api.json_responses import AuthResponse


def register_handler(request: WSGIRequest) -> JsonResponse:
    if request.method == "POST":
        if request.user.is_authenticated:
            response = AuthResponse.userAuthenticated

        elif "username" not in request.POST or \
             "password" not in request.POST or \
             "email"    not in request.POST:
            response = AuthResponse.invalidArgs

        elif User.objects.filter(username=request.POST["username"]).exists():
            response = AuthResponse.Register.profileExists

        else:
            register_user(request)
            response = AuthResponse.success

    else:
        response = AuthResponse.methodError
    
    return JsonResponse({"data":response})


def login_handler(request: WSGIRequest) -> JsonResponse:
    if not request.POST:
        response = AuthResponse.methodError

    elif request.user.is_authenticated:
        response = AuthResponse.userAuthenticated

    elif not request.POST.get("username", True) and request.POST.get("password", True):
        response = AuthResponse.invalidArgs

    else:
        errors = is_authentication_success(request)
        if errors:
            response = AuthResponse.Login.incorrectData

        else:
            response = AuthResponse.success

    return JsonResponse({"data":response})


def verify_email_user(request : WSGIRequest, profile_id : str, auth_key : str) -> JsonResponse:
    is_verify_needed = ProfilesToVerify.objects.filter(profile_id=profile_id)[0]
    profile = Profile.objects.filter(profile_id=profile_id)[0]
    if not profile:
        response = AuthResponse.EmailVerify.profileNotExistResponse

    elif not is_verify_needed or profile.is_verifyied:
        response = AuthResponse.EmailVerify.profileVerifyiedResponse

    elif is_verify_needed and ProfilesToVerify.auth_key != auth_key:
        response = AuthResponse.EmailVerify.authKeyErrorResponse

    elif is_verify_needed and ProfilesToVerify.auth_key == auth_key:

        profile.is_verifyied = True
        ProfilesToVerify.objects.filter(profile_id=profile_id).delete()
        response = AuthResponse.EmailVerify.verifySuccessResponse

    return JsonResponse({"data" : response})


def logout_hanlder(request: WSGIRequest) -> HttpResponseRedirect:
    logout(request)
    return redirect('home')


def recovery_password_handler(request):
    pass