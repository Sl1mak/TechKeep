from django.db import models
from django.conf import settings

class Room(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=6, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms', blank=True)

    def __str__(self):
        return self.name

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

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField(max_length=500)
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