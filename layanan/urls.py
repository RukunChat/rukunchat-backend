from django.urls import path
from .views import *

app_name = 'layanan'

urlpatterns = [
    path('all/', show_all_layanan, name='show_all_layanan'),
    path('add/', add_layanan, name='add_layanan'),
]