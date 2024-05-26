from django.db import models
from users.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_name} favorited by {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.JSONField()  # JSON field to store ordered products details

    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product_name} in {self.user.username}'s cart"
