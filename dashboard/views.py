from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


@login_required(login_url='Вход')
def index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='Вход')
def market(request):
    return render(request, 'dashboard/market.html')


@login_required(login_url='Вход')
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Продукты')
    else:
        form = ProductForm()
    context={
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)


@login_required(login_url='Вход')
def order(request):
    return render(request, 'dashboard/order.html')


@login_required(login_url='Вход')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Продукты')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required(login_url='Вход')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Продукты')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)