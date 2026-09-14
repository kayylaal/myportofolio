from django.shortcuts import render
from main.models import Project, SocialWork

def show_main(request):
    context = {
        "name": "Kayla",
        "npm": "2506603854",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year information Systems student at University of Indonesia."
        ),
    }
    return render(request, "index.html", context)

def show_experiences(request):
    context = {
        "name": "Kayla",
        "projects": Project.objects.all(),
        "social_works": SocialWork.objects.all(),
    }
    return render(request, "experiences.html", context)
