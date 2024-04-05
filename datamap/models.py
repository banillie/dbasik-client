from django.db import models

class Datamap(models.Model):
    name = models.CharField(max_length=56, blank=False, null=False)
    description = models.CharField(max_length=256, blank=True, null=True)
