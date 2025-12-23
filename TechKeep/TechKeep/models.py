from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('under_review', 'Поступил в обработку'),
        ('diagnosing_issue', 'Выявление проблемы'),
        ('repairing', 'Ремонт'),
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

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField(max_length=500)
    diagnosting_description = models.TextField(max_length=500, blank=True)
    repairing_description = models.TextField(max_length=500, blank=True)
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