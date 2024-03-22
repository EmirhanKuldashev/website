from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

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
