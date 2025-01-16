from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        managed = True
        db_table = "user"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = "product"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = "order"
