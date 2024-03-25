from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Category

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def current_date_view(request):
    if request.method == 'GET':
        from datetime import datetime
        return HttpResponse(f"Current date: {datetime.today().strftime('%Y-%m-%d')}")

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")

def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def product_list_view(request):
    products = Product.objects.all
    context = {'products': products}
    return render(request, 'product/product_list.html', context)

def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    context = {'product': product}

    return render(request, 'product/product_detail.html', context)

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/categories.html', context)
