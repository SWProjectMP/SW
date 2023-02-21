from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def profile_view(request):
    if request.user.is_anonymous or not request.user:
        return redirect('home')
    return render(request, "profile_system/profile.html", {"user":request.user})