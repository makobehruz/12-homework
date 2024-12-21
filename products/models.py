from django.db import models



class Product(models.Model):
    nomi = models.CharField(max_length=100)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    kategoriya = models.CharField(max_length=50)

