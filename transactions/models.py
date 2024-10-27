from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Название категории', max_length = 160)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'categories')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/categories/{self.id}'
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Transaction(models.Model):
    TYPES_OF_TRANSACTIONS = [
        ('income', 'Доход'),
        ('expense', 'Расход'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'transactions')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'transactions')
    type_of_transaction = models.CharField(max_length = 7, choices = TYPES_OF_TRANSACTIONS)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField()
    description = models.TextField(max_length = 300, blank = True)
    
    def __str__(self):
        return f"{self.type_of_transaction} – {self.amount}"
    
    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"


class Goal(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'goals')
    target_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    current_amount = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    deadline = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Финансовая цель"
        verbose_name_plural = "Финансовые цели"