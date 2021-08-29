from django.db import models


class Team(models.Model):
    image = models.ImageField(balnk=True, upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    google_plus_link = models.URLField(blank=True, null=True)
