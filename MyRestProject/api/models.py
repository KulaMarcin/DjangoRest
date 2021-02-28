from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.IntegerField
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    engine_type = models.CharField(max_length=20)
    price = models.IntegerField

    def __str__(self):
        return self.manufacturer
