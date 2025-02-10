import os
import django
from django.utils.timezone import now

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab4.settings")
django.setup()

from myapp.models import Category, Product, Client, Order

# --- CATEGORIES ---
categories = [
    ("Furniture", "Windsor"),
    ("Appliances", "Windsor"),
    ("Electronics", "London"),
    ("Home Decor", "Waterloo"),
    ("Flooring", "London"),
]

print("Adding Categories...")
for name, warehouse in categories:
    category, created = Category.objects.get_or_create(name=name, warehouse=warehouse)
    if created:
        print(f"Added Category: {name} in {warehouse}")
    else:
        print(f"Category already exists: {name} in {warehouse}")


# --- CLIENTS ---
clients = [
    ("john", "John", "Smith", "123 University Avenue", "Windsor", "ON", ["Furniture", "Home Decor"]),
    ("mary", "Mary", "Hall", "456 Sunset Avenue", "Windsor", "ON", ["Furniture", "Electronics"]),
    ("alan", "Alan", "Jones", "789 King Street", "Calgary", "AB", ["Appliances", "Home Decor"]),
    ("josh", "Josh", "Jones", "456 Sunset Avenue", "Montreal", "QC", ["Furniture", "Home Decor"]),
    ("bill", "Bill", "Wang", "987 King Street", "Edmonton", "AB", ["Electronics"]),
]

print("\nAdding Clients...")
for username, first_name, last_name, address, city, province, interests in clients:
    client, created = Client.objects.get_or_create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        shipping_address=address,
        city=city,
        province=province,
    )
    if created:
        client.set_password(username)  # Use username as password
        client.save()
        print(f"Added Client: {first_name} {last_name}")
    else:
        print(f"Client already exists: {first_name} {last_name}")

    # Assign interested categories dynamically
    for category_name in interests:
        category = Category.objects.filter(name=category_name).first()
        if category:
            client.interested_in.add(category)
        else:
            print(f"Category not found: {category_name}")


# --- PRODUCTS ---
products = [
    ("Clock", "Home Decor", 99.99, 50),
    ("Vase", "Home Decor", 82.54, 100),
    ("Painting", "Home Decor", 135.80, 80),
    ("Lamp", "Home Decor", 59.99, 200),
    ("Tablet", "Electronics", 299.99, 0),
    ("Laptop", "Electronics", 975.50, 85),
    ("TV", "Electronics", 3500.00, 20),
    ("Table", "Furniture", 599.99, 120),
    ("Dresser", "Furniture", 360.85, 100),
    ("Bed", "Furniture", 1225.25, 0),
    ("Sofa", "Furniture", 1500.95, 175),
    ("Dryer", "Appliances", 775.00, 0),
    ("Washer", "Appliances", 885.75, 50),
    ("Stove", "Appliances", 950.50, 50),
]

print("\nAdding Products...")
for name, category_name, price, stock in products:
    category = Category.objects.filter(name=category_name).first()
    if category:
        product, created = Product.objects.get_or_create(
            name=name,
            category=category,
            defaults={
                "price": price,
                "stock": stock,
                "available": stock > 0,  # Mark as available if stock > 0
            },
        )
        if created:
            print(f"Added Product: {name}")
        else:
            print(f"Product already exists: {name}")
    else:
        print(f"Category not found for product: {name}")


# --- ORDERS ---
orders = [
    ("Lamp", "mary", 2),
    ("TV", "john", 1),
]

print("\nAdding Orders...")
for product_name, client_username, num_units in orders:
    product = Product.objects.filter(name=product_name).first()
    client = Client.objects.filter(username=client_username).first()

    if product and client:
        order, created = Order.objects.get_or_create(
            product=product,
            client=client,
            num_units=num_units,
            defaults={"status_date": now()},  # Set status_date dynamically
        )
        if created:
            print(f"Added Order: {num_units} {product_name}(s) for {client_username}")
        else:
            print(f"Order already exists: {num_units} {product_name}(s) for {client_username}")
    else:
        if not product:
            print(f"Product not found: {product_name}")
        if not client:
            print(f"Client not found: {client_username}")


print("\n Database populated successfully!")
