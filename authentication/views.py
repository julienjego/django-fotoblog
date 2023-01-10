from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from . import forms


# Définition de la vue par une classe
class LoginPageView(View):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, {"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")

        message = "Identifiants invalides."

        return render(
            request, "authentication/login.html", {"form": form, "message": message}
        )


# Définition de la même vue par une fonction
# def login_page(request):
#     form = forms.LoginForm()
#     message = ""
#     if request.method == "POST":
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")

#         message = "Identifiants invalides."

#     return render(
#         request, "authentication/login.html", {"form": form, "message": message}
#     )


def logout_user(request):
    logout(request)
    return redirect("login")


def signup_page(request):
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentication/signup.html", {"form": form})
