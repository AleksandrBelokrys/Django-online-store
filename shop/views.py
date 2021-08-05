from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'shop/home.html')


def product(request):
    return render(request, 'shop/product.html')
