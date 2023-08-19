from django.db import models

from accounts.models import Account
from shop.models import Product


# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE) #작성자
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #상품
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)

    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)