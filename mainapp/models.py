from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    github_url = models.URLField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length=512, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
