from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                message = f"""Bonjour {user.username} ! 
                Vous êtes bien connecté."""
                login(request, user)
            else:
                message = "Identifiants invalides."

    return render(
        request, "authentication/login.html", {"form": form, "message": message}
    )


def logout_user(request):
    logout(request)
    return redirect("login")
