from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    dot=models.DateTimeField()
    body=models.TextField()
    imgs=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:50]
    def dot_new(self):
        return self.dot.strftime('%b %e %Y')
