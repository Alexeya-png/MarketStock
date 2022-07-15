from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='Вход')
def index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='Вход')
def market(request):
    return render(request, 'dashboard/market.html')


@login_required(login_url='Вход')
def product(request):
    return render(request, 'dashboard/product.html')


@login_required(login_url='Вход')
def order(request):
    return render(request, 'dashboard/order.html')
