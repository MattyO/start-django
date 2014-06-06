from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

from common.helpers import resolve_http_method
from common.forms import UserRegistrationForm 

def index(request):
    return render(request, "index.html")

@login_required
def user_profile(request):
    c={"current_user":request.user}
    return render(request, "accounts/profile.html", c)

def register(request):
    new_user_form = UserRegistrationForm()
    c = { "registration_form": new_user_form }
    c.update(csrf(request))

    def get():
        return render(request, 'registration/register.html', c)

    def post():
        new_user_form = UserRegistrationForm(request.POST)
        c.update({ "registration_form": new_user_form })
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect("login")
        return render(request, 'registration/register.html', c)

    return resolve_http_method(request, [get, post])
