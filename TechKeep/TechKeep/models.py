from django.db import models
from django.conf import settings

class Product(models.Model):
    STATUS_CHOICES = [
        ('under_review', 'Поступил в обработку'),
        ('testing', 'Тестирование'),
        ('ready_for_pickup', 'Готов к использованию'),
    ]

    CATEGORY_CHOICES = [
        ('mobile', 'Смартфоны'),
        ('tablet', 'Планшеты'),
        ('laptop', 'Ноутбуки'),
        ('pc', 'Компьютеры'),
        ('accessories', 'Аксессуары'),
        ('electronics', 'Электроника'),
        ('other', 'Другое'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField(max_length=500)
    diagnosting_description = models.TextField(max_length=500, blank=True)
    testing_description = models.TextField(max_length=500, blank=True)
    type = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        default='other'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='under_review'
    )

    def __str__(self):
        return self.name