from django.db import models


class Press(models.Model):
    press_id = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=10)
    category = models.CharField(max_length=20)

