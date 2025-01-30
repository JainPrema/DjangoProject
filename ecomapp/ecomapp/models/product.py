from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()


class dairyProducts(Product):
    expiry_date = models.DateField(
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        db_table = 'dairy_products'

