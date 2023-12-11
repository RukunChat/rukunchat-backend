from django.urls import path
from .views import show_all_forum, add_forum, reply_forum, forum_detail

app_name = 'forum'

urlpatterns = [
    path('all/', show_all_forum, name='show_all_forum'),
    path('add/', add_forum, name='add_forum'),
    path('reply/<int:forum_id>/', reply_forum, name='reply_forum'),
    path('detail/<int:forum_id>/', forum_detail, name='forum_detail'),
]