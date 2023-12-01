from django.urls import path
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
]