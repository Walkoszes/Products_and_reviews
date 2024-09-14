from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.author} - {self.rating}"