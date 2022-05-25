import datetime

from django.db import models


class AppKind(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class AppAgeLimit(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=500)
    min_age = models.SmallIntegerField

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=256, null=False)
    desc = models.CharField(max_length=3000, null=False)
    kind = models.ForeignKey(AppKind, on_delete=models.CASCADE)
    age_limit = models.ForeignKey(AppAgeLimit, on_delete=models.CASCADE)
    download_counter = models.PositiveBigIntegerField(default=0)
    last_update = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.name
