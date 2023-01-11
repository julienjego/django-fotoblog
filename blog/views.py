from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "blog/home.html")


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # ajoute l'identité de l'uploader
            photo.upload = request.user
            # on sauvegarde
            photo.save()
            return redirect("home")
    return render(request, "blog/photo_upload.html", {"form": form})
