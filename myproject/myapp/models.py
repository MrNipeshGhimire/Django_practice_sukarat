from django.db import models

# Create your models here.
# authentication, authorization, security
# 1047779393.00

# product table 
class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
