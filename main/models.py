from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class SocialWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    organization_name = models.CharField(max_length=255)
    organization_logo = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.role} at {self.organization_name}"