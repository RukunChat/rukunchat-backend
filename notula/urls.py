from django.urls import path
from .views import *

app_name = 'notula'

urlpatterns = [
   path("add/", views.add_notula, name="add_notula"),
   path('<int:id_notula>/', notula_detail, name='notula_detail'),
]