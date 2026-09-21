from django.urls import path
from main.views import (
    show_main,
    show_experiences,
    create_project,
    update_project,
    show_projects,
    get_projects_json,
    delete_project,
    show_socialworks,
    get_socialworks_json,
    create_socialworks,
    update_socialworks,
    delete_socialworks,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experiences/", show_experiences, name="show_experiences"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<int:project_id>/edit/", update_project, name="update_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path("socialworks/", show_socialworks, name="show_socialworks"),
    path("api/socialworks/", get_socialworks_json, name="get_socialworks_json"),
    path("socialworks/add/", create_socialworks, name="create_socialworks"),
    path("socialworks/<int:socialwork_id>/edit/", update_socialworks, name="update_socialworks"),
    path("socialworks/<int:socialwork_id>/delete/", delete_socialworks, name="delete_socialworks"),
]
