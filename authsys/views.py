from django.shortcuts import render
from django.shortcuts import redirect
from api.models import Profile, ProfilesToVerify
# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'authsys/registration_page.html')
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'authsys/login_page.html')
def forgot_pass_view(request):
    pass

def verify_email(request, profile_id, auth_key):
    return render(request, 'authsys/email_verufy.html', {"profile_id": profile_id, "auth_key" : auth_key})