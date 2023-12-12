from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255)
    num_responses = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class ForumResponse(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='responses')
    response_text = models.TextField()
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    response_date = models.DateTimeField(auto_now_add=True)
