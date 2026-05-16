from django.db import models

class Cars(models.Model):
    model = models.TextField(max_length=20)
    price = models.TextField(max_length=20)
    color = models.TextField(max_length=20)                                                         