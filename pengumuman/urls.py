from django.urls import path
from .views import *

app_name = 'pengumuman'

urlpatterns = [
    path('', pengumuman_list, name='pengumuman_list'),

]