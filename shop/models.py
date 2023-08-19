from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Account
from config import settings


# Create your models here.
# 상품 모델
class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True) # 상품 이름

    slug = models.SlugField(max_length=50, db_index=True, allow_unicode=True) # 슬러그

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default='default.png') # 상품 이미지
    description = models.TextField(blank=True) # 상품 설명
    meta_description = models.TextField(blank=True)

    delivery_date = models.IntegerField() # 배송일

    price = models.IntegerField() # 상품 가격
    stock = models.PositiveIntegerField() # 상품 재고

    available_display = models.BooleanField('Display', default=True) # 상품 전시
    available_order = models.BooleanField('Order', default=True) # 상품 주문

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.id, self.slug])

# 할인
class Discount(models.Model):
    discount_price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    active = models.BooleanField()