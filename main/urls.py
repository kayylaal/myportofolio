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
    register,
    login_user,
    logout_user,
    toggle_star,
    toggle_socialwork_star,
    create_project_ajax,
    create_socialwork_ajax,
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
    # crud + json social works
    path("socialworks/", show_socialworks, name="show_socialworks"),
    path("api/socialworks/", get_socialworks_json, name="get_socialworks_json"),
    path("socialworks/add/", create_socialworks, name="create_socialworks"),
    path("socialworks/<int:socialwork_id>/edit/", update_socialworks, name="update_socialworks"),
    path("socialworks/<int:socialwork_id>/delete/", delete_socialworks, name="delete_socialworks"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path("socialworks/<int:socialwork_id>/star/", toggle_socialwork_star, name="toggle_socialwork_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("socialworks/add-ajax/", create_socialwork_ajax, name="create_socialwork_ajax"),
]
