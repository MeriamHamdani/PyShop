from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# django is a package, shortcuts is a module and render is a function


def index(request):
    products =  Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Hello this is a new day u should thank GOD u still alive u have chance)')