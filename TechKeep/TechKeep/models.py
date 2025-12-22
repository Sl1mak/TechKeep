from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('under_review', 'Поступил в обработку'),
        ('diagnosing_issue', 'Выявление проблемы'),
        ('repairing', 'Ремонт'),
        ('testing', 'Тестирование'),
        ('ready_for_pickup', 'Готов к использованию'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    diagnosting_description = models.TextField(max_length=500)
    repairing_description = models.TextField(max_length=500)
    testing_description = models.TextField(max_length=500)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='under_review'
    )

    def __str__(self):
        return self.name