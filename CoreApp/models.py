from django.db import models


# Create your models here.

class Order(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=4)
    merchant_id = models.CharField(max_length=36)
    merchant_order_id = models.CharField(max_length=36)
    tracking_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
