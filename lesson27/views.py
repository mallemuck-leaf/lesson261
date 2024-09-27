from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.


def task_page(request):
    return render(request, 'lesson27/lesson27.html')


def product_page(request):
    content = {
        'products': Product.objects.all(),
    }
    # [print(x) for x in Product.objects.all()]
    return render(request, 'lesson27/lesson_products.html', content)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(name=request.POST.get('name'),
                                   price=request.POST.get('price'))
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            # form.save()
        return redirect('/lesson27/task3/')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'lesson27/lesson_add_product.html', context)

