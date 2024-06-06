from django.db import models

class Repository(models.Model):
    repo_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.name