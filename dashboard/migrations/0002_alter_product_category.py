# Generated by Django 4.0.6 on 2022-07-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Крупы и макароны', 'Крупы и макароны'), ('Овощи и фрукты', 'Овощи и фрукты'), ('Мучное', 'Мучное'), ('Мясо и яйца', 'Мясо и яйца'), ('Алкогольные напитки', 'Алкогольные напитки'), ('Сладости', 'Сладости'), ('Рыба и морепродукты', 'Рыба и морепродукты'), ('Красота и здоровье', 'Красота и здоровье'), ('Хозяйственные товары', 'Хозяйственные товары'), ('Дом и сад', 'Дом и сад'), ('Молочные продукты', 'Молочные продукты'), ('Напитки', 'Напитки'), ('Замороженное', 'Замороженное')], max_length=20, null=True),
        ),
    ]
