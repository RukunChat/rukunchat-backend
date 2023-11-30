from django.urls import path
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
]