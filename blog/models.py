from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    dot=models.DateTimeField()
    body=models.TextField()
    imgs=models.ImageField(upload_to='images/')
