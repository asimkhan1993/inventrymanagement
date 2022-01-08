from django.db import models

# Create your models here.


class Item(models.Model):
    product_name = models.CharField(max_length=100)
    product_num = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    unit_measure = models.CharField(max_length=10)
    packing_type = models.CharField(max_length=100)
