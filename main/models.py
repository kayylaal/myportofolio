from django.db import models

# untuk menyimpan data projects
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# untuk menyimpan data social works
class SocialWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.URLField(blank=True, null=True)
    # tahun kegiatan, integer biar tipe datanya tidak string semua
    year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title