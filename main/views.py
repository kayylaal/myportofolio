from django.shortcuts import render


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