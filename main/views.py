from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from main.models import Project, SocialWork
from main.forms import ProjectForm, SocialWorkForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied       
from django.views.decorators.http import require_POST

def is_editor(user):
    return user.is_authenticated and (
        user.is_superuser or user.groups.filter(name="Editor").exists()
    )

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account successfully created! Please login ><")
        return redirect("main:login")

    context = {
        "name": "Kayla Ali",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect(request.GET.get("next") or "main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session yet/Cookie not found')
    context = {
        "name": "Kayla",
        "npm": "2506603854",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year information Systems student at University of Indonesia."
        ),
        "projects": Project.objects.all(),
        "social_works": SocialWork.objects.all(),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experiences(request):
    context = {
        "name": "Kayla",
        "projects": Project.objects.all(),
        "social_works": SocialWork.objects.all(),
    }
    return render(request, "experiences.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Kayla",
        "form": form,
        "is_update": False,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not is_editor(request.user):
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diubah!")
        return redirect("main:show_projects")

    context = {
        "name": "Kayla",
        "form": form,
        "is_update": True,
        "project": project,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def create_socialworks(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = SocialWorkForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Social Work baru berhasil ditambahkan!")
        return redirect("main:show_socialworks")

    context = {
        "name": "Kayla",
        "form": form,
        "is_update": False,
    }
    return render(request, "socialworks_form.html", context)

@login_required(login_url="/login/")
def update_socialworks(request, socialwork_id):
    if not is_editor(request.user):
        raise PermissionDenied
    
    socialwork = get_object_or_404(SocialWork, pk=socialwork_id)
    # instance agar form mengedit data yang sudah ada
    form = SocialWorkForm(request.POST or None, instance=socialwork)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Social Work berhasil diubah!")
        return redirect("main:show_socialworks")

    context = {
        "name": "Kayla",
        "form": form,
        "is_update": True,
        "socialwork": socialwork,
    }
    return render(request, "socialworks_form.html", context)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Kayla",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)


def show_socialworks(request):
    context = {
        "name": "Kayla",
        "is_editor": is_editor(request.user),
        "form": SocialWorkForm(),
    }

    return render(request, "socialworks.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "link": project.link,
                "thumbnail": project.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

# susun json manual + info star
def get_socialworks_json(request):
    title_query = request.GET.get("title", "").strip()
    socialworks = SocialWork.objects.prefetch_related('starred_by').all()

    # filter judul kalau ada query ?title=
    if title_query:
        socialworks = socialworks.filter(title__icontains=title_query)

    data = []
    for sw in socialworks:
        starred_users = sw.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(sw.id),
            "fields": {
                "title": sw.title,
                "description": sw.description,
                "photo": sw.photo,
                "year": sw.year,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def delete_socialworks(request, socialwork_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    socialwork = get_object_or_404(SocialWork, pk=socialwork_id)

    if request.method == "POST":
        socialwork.delete()
        messages.success(request, "Social Work berhasil dihapus!")
        return redirect("main:show_socialworks")

    return redirect("main:show_socialworks")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_socialwork_star(request, socialwork_id):
    socialwork = get_object_or_404(SocialWork, pk=socialwork_id)

    if request.method == "POST":
        if request.user in socialwork.starred_by.all():
            socialwork.starred_by.remove(request.user)
        else:
            socialwork.starred_by.add(request.user)

    return redirect("main:show_socialworks")


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)