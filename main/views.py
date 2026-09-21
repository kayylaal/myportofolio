from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Project, SocialWork
from main.forms import ProjectForm, SocialWorkForm
from django.contrib import messages


def show_main(request):
    context = {
        "name": "Kayla",
        "npm": "2506603854",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year information Systems student at University of Indonesia."
        ),
        "projects": Project.objects.all(),
        "social_works": SocialWork.objects.all(),
    }
    return render(request, "index.html", context)


def show_experiences(request):
    context = {
        "name": "Kayla",
        "projects": Project.objects.all(),
        "social_works": SocialWork.objects.all(),
    }
    return render(request, "experiences.html", context)


def create_project(request):
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


def update_project(request, project_id):
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

def create_socialworks(request):
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


def update_socialworks(request, socialwork_id):
    socialwork = get_object_or_404(SocialWork, pk=socialwork_id)
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
    json_response = get_projects_json(request)
    project_list = []
    for obj in serializers.deserialize("json", json_response.content):
        project_list.append(obj.object)

    context = {
        "name": "Kayla",
        "project_list": project_list,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)


def show_socialworks(request):
    title_query = request.GET.get("title", "").strip()
    json_response = get_socialworks_json(request)
    socialwork_list = []
    for obj in serializers.deserialize("json", json_response.content):
        socialwork_list.append(obj.object)

    context = {
        "name": "Kayla",
        "socialwork_list": socialwork_list,
        "title_query": title_query,
    }
    return render(request, "socialworks.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def get_socialworks_json(request):
    title_query = request.GET.get("title", "").strip()
    socialworks = SocialWork.objects.all()

    if title_query:
        socialworks = socialworks.filter(title__icontains=title_query)

    socialworks_json = serializers.serialize("json", socialworks)
    return HttpResponse(socialworks_json, content_type="application/json")


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def delete_socialworks(request, socialwork_id):
    socialwork = get_object_or_404(SocialWork, pk=socialwork_id)

    if request.method == "POST":
        socialwork.delete()
        messages.success(request, "Social Work berhasil dihapus!")
        return redirect("main:show_socialworks")

    return redirect("main:show_socialworks")