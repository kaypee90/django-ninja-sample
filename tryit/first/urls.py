from django.urls import path
from first.api import api

app_name = "first"

urlpatterns = [
    path("api/", api.urls),
]