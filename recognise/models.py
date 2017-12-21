from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    image = models.FileField()
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


