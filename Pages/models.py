from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=8)
    explanation = models.CharField(max_length=35)
    # price = models.FloatField(max_length=5)

    def __str__(self):
        return self.name
  