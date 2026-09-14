from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Kayla",
        "npm": "2506603854",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year information Systems student at University of Indonesia."
        ),
        "experiences": Experience.objects.all(),
    }
    return render(request, "index.html", context)