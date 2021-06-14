from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    image = models.CharField(max_length=1000,
                             default="https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")

    def __str__(self):
        return self.name
