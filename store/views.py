from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.
def store(request):
    all_products = Product.objects.all()
    return render(request, 'store/store.html', {'products': all_products})


def categories(request):
    all_categories = Category.objects.all()
    return {'categories': all_categories}


def product_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product_page.html', context)


def category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category__name=category)
    return render(request, 'store/category_page.html',  {"category": category, "category_products": products})


