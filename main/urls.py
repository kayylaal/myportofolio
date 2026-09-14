from django.urls import path

from main.views import show_main, show_experiences

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experiences/", show_experiences, name="show_experiences"),
]
