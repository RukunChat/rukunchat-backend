from django.urls import path

from . import views

app_name = "agenda"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_kegiatan, name="add_kegiatan"),
    path("<int:kegiatan_id>/", views.detail, name="detail"),
]