from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product, Category, Review
from product.forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

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
    products = Product.objects.all()
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


def product_create_view(request):
    if request.method == 'GET':
        return render(request, 'product/product_create.html')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'product/product_create.html', {'form': form})

        product = Product.objects.create(
            name=form.cleaned_data.get('name'),
            price=form.cleaned_data.get('price'),
            image=form.cleaned_data.get('image'),
            rate=form.cleaned_data['rate'],
        )

    return redirect('product_list')

@login_required
def review_create_view(request, product_pk):
    product = Product.objects.get(pk=product_pk)

    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'review/review_create.html', {'form': form, 'product': product})

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'review/review_create.html', {'form': form, 'product': product})

        review = Review.objects.create(
            product=product,
            user=request.user,
            text=form.cleaned_data['text'],
        )

        return redirect('product_detail', product.pk)

