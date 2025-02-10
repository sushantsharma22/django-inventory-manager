# Import necessary classes and functions
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category, Product


def index(request):

    cat_list = Category.objects.all().order_by('id')[:10]

    product_list = Product.objects.all().order_by('-price')[:5]

    response = HttpResponse()

    heading_categories = '<p><strong>List of Categories:</strong></p>'
    response.write(heading_categories)
    for category in cat_list:
        para = f'<p>{category.id}: {category}</p>'
        response.write(para)

    heading_products = '<p><strong>List of up to 5 Products (Most Expensive First):</strong></p>'
    response.write(heading_products)
    for product in product_list:
        para = f'<p>{product.id}: {product} - ${product.price}</p>'
        response.write(para)

    return response

def about(request):
    return HttpResponse("This is an Online Store APP.")

def detail(request, cat_no):
    # Use get_object_or_404 to return a 404 error if the category does not exist.
    category = get_object_or_404(Category, id=cat_no)

    # Retrieve the warehouse field
    warehouse_location = getattr(category, 'warehouse', 'Unknown')

    # Retrieve all products associated with this category.
    product_list = Product.objects.filter(category=category)

    response = HttpResponse()
    header = f'<p><strong>Warehouse Location for Category {category.id}:</strong> {warehouse_location}</p>'
    response.write(header)

    product_header = '<p><strong>List of Products in this Category:</strong></p>'
    response.write(product_header)

    for product in product_list:
        para = f'<p>{product.id}: {product} - ${product.price}</p>'
        response.write(para)

    return response

