from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    cart_count = models.IntegerField(default=0)
