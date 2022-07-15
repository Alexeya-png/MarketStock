from django.contrib import admin
from django.urls import path
import dashboard.views

urlpatterns = [
    path('', dashboard.views.index, name='Главная страница'),
    path('market/', dashboard.views.market, name='Супермаркеты'),
    path('product/', dashboard.views.product, name='Продукты'),
    path('order/', dashboard.views.order, name='Поставки')
]
