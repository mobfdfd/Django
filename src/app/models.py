from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=200)
    article = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.stock} x {self.brand} - {self.article}"

class Customer(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.brand} - {self.product.article} in {self.customer}'