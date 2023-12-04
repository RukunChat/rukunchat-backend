from django.urls import path
from .views import show_all_forum, add_forum

app_name = 'forum'

urlpatterns = [
    path('all/', show_all_forum, name='show_all_forum'),
    path('add/', add_forum, name='add_forum'),
]
