from django.urls import path
from main.views import show_main, show_experiences, create_project, show_projects, get_projects_json, delete_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experiences/", show_experiences, name="show_experiences"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project")
]
