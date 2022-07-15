from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Крупы и макароны', 'Крупы и макароны'),
    ('Овощи и фрукты', 'Овощи и фрукты'),
    ('Мучное', 'Мучное'),
    ('Мясо и яйца', 'Мясо и яйца'),
    ('Алкогольные напитки', 'Алкогольные напитки'),
    ('Сладости', 'Сладости'),
    ('Рыба и морепродукты', 'Рыба и морепродукты'),
    ('Красота и здоровье', 'Красота и здоровье'),
    ('Хозяйственные товары', 'Хозяйственные товары'),
    ('Дом и сад', 'Дом и сад'),
    ('Молочные продукты', 'Молочные продукты'),
    ('Напитки', 'Напитки'),
    ('Замороженное', 'Замороженное'),

)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20 , choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)


    def __str__(self):
        return f'{self.name}-{self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    market = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} заказано {self.market.username}'
