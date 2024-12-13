from django.db import models

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()

    def __str__(self):
        return f"{self.author}: {self.content[:20]}"