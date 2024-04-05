from django.db import models

class Datamap(models.Model):
    name = models.CharField(max_length=56, blank=False, null=False)
    description = models.CharField(max_length=256, blank=True, null=True)

class DatamapLine(models.Model):
    dm = models.ForeignKey(Datamap, on_delete=models.CASCADE, blank=False)
    key = models.CharField(max_length=56, blank=False, null=False)
    sheet = models.CharField(max_length=56, blank=False, null=False)
    cellref = models.CharField(max_length=5, blank=False, null=False)

