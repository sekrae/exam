from itertools import product
from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Category,Product
from django.http import HttpResponse

def product_view(request):
    product = Product.objects.all()
    return render(request, 'render.html', {'product': product})

def detail_view(request, id):
    product_detail = Product.objects.get(id=id)
    return render(request, 'single_product.html', {'product_detail': product_detail})

def delete_view(request, id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return HttpResponse("товар удалён")

def create_view(request):
    
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories': categories })

    if request.method == "POST":
        name = request.POST.get('name')
        categories = request.POST.get('categories')
        unique_number = request.POST.get('unique_number')
        initial_cost = request.POST.get('initial_cost')
        residual_value = request.POST.get('residual_value')
        category_id = request.POST.get('cotegory')
        
        categories = Category.objects.get(id=category_id)
        new_product = Product(
            name = name,
            categories = categories,
            unique_number = unique_number,
            initial_cost = initial_cost,
            residual_value = residual_value,
            category = category,
            )  
        new_product.save()

        return redirect(reverse('all_category'))

    
def update_view(request, id):
    products = Product.objects.get(id=id)
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'products': products,
        }
        return render(request, 'update.html', context)

    if request.method == "POST":
        name = request.POST.get('name')
        categoryies = request.POST.get('categories')
        unique_number = request.POST.get('unique_number')
        initial_cost = request.POST.get('initial_cost')
        residual_value= request.POST.get('residual_value')
        category_id = request.POST.get('category')
        
        categories = Category.objects.get(id=category_id)

        product.name = name
        product.categories = categories
        product.unique_number = unique_number
        product.initial_cost = initial_cost
        product.residual_value = residual_value
        product.cotegory_id = category_id


        product.save()

        return redirect(reverse('all_product'))


