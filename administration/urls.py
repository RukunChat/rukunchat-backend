from django.urls import path
from .views import *

app_name = 'administration'

urlpatterns = [
    path('update-profile/', update_profile, name='update_profile'),

]