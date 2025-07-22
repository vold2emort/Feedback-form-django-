from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, ListView
import os

from .models import UserProfiles
# Create your views here.

def store_file(file):
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    with open(os.path.join(temp_dir, "image.jpg"), "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html", {"form": form})

    # def post(self, request):
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #     if submitted_form.is_valid():
    #         profile = UserProfiles(image=request.FILES["user_image"])
    #         profile.save()
    #         return HttpResponseRedirect("/thank_you")
        
    #     return render(request, "profiles/create_profile.html", {"form": submitted_form})
    template_name = "profiles/create_profile.html"
    success_url = "/thank_you"
    model = UserProfiles
    fields = "__all__"

class ProfileView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfiles
    context_object_name = "profiles"
    