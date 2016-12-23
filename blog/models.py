from django.db import models


class Momo(models.Model):
    name = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=150, default='')
    image = models.ImageField(blank=False, upload_to='media/momos', default='')
