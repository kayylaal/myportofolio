from django.db import models
from django.contrib.auth.models import User

# untuk menyimpan data projects
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    def __str__(self):
        return self.title

# untuk menyimpan data social works
class SocialWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.URLField(blank=True, null=True)
    # tahun kegiatan, integer biar tipe datanya tidak string semua
    year = models.PositiveIntegerField(blank=True, null=True)
    # field buat star, manytomany karena 1 field bisa beberapa user
    starred_by = models.ManyToManyField(
            User, related_name="starred_socialworks", blank=True
        )

    def __str__(self):
        return self.title