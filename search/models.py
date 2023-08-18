from django.db import models
from accounts.models import Account


# Create your models here.

class SearchHistory(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query