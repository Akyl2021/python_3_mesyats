from itertools import product

from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Review, Category


# Create your views here.

def test(request):
    return HttpResponse(b'<h1>Hello WORLD</h1')


def index(request):
    products = Product.objects.all()
    data = {
        'title': 'Продукты',
        'products': products
    }
    return render(request, 'index.html', context=data)


def product_item(request, id):
    products = Product.objects.get(id=id)
    date = request.GET.get('date')
    review = Review.objects.filter(product_id=id)
    if date != None:
        review = Review.objects.filter(product_id=id, date__gte=date).exclude(text__icontains='niger')
    data = {
        'products': products,
        'review': review
    }

    return render(request, 'product.html', context=data)


def category_in(request, id):
    category = Category.objects.get(id=id)
    data = {
        'category': category
    }
    return render(request, 'category.html', context=data)


def review_list(request):
    text = request.GET.get('search_text')
    products = Product.objects.filter(name__contains=text)
    return render(request, 'product.html', context={
        'products': products
    })
