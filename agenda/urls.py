from django.urls import path

from . import views

app_name = "agenda"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:kegiatan_id>/", views.detail, name="detail"),
]