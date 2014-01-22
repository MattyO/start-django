from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

from common.helpers import resolve_http_method

def index(request):
    return render(request, "index.html")

@login_required
def user_profile(request):
    return render(request, "accounts/profile.html")

def register(request):
    new_user_form = UserCreationForm()
    c = { "registration_form": new_user_form }
    c.update(csrf(request))

    def get():
        return render(request, 'common/register.html', c)

    def post():
        new_user_form = UserCreationForm(request.POST)
        c.update({ "registration_form": new_user_form })
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect("login")
        return render(request, 'common/register.html', c)

    return resolve_http_method(request, [get, post])
