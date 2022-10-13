from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)



