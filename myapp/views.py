# Import necessary classes and functions
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Category

def index(request):
    # Query the first 10 categories ordered by id.
    cat_list = Category.objects.all().order_by('id')[:10]
    # Pass the context variable 'cat_list' to the template.
    return render(request, 'myapp/index0.html', {'cat_list': cat_list})

# The about view (initial version uses about0.html)
def about(request):
    return render(request, 'myapp/about0.html')

# The detail view for a specific category (initial version uses detail0.html)
def detail(request, cat_no):
    # Retrieve the category with id=cat_no
    cat = get_object_or_404(Category, id=cat_no)
    # Assume a related name "products" for the products belonging to the category.
    product_list = cat.products.all() if hasattr(cat, 'products') else []
    return render(request, 'myapp/detail0.html', {'cat': cat, 'product_list': product_list})


def welcome(request):
    return HttpResponse("Welcome to the Online Store!")
