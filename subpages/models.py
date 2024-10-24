# subpages/models.py

from django.db import models
from casinos.models import Casino

class Subpage(models.Model):
    title = models.CharField(max_length=100)
    css_file = models.CharField(max_length=100)  # Name of the CSS file for the subpage
    casinos = models.ManyToManyField(Casino, through='SubpageCasino')  # Define through model for ManyToMany relationship
    youtube = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitch = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    dlive = models.URLField(max_length=200, null=True, blank=True)
    kick = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class SubpageCasino(models.Model):
    subpage = models.ForeignKey(Subpage, on_delete=models.CASCADE)
    casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
    affiliate_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.subpage.title} - {self.casino.name}"
