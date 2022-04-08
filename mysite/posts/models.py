from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    published = models.BooleanField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
