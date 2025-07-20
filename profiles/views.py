from django.shortcuts import render, HttpResponseRedirect
from django.views import View
import os
from .forms import ProfileForm
from .models import UserProfiles
# Create your views here.

def store_file(file):
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    with open(os.path.join(temp_dir, "image.jpg"), "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfiles(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/thank_you")
        
        return render(request, "profiles/create_profile.html", {"form": submitted_form})