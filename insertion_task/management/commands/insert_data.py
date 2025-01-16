import threading
from django.core.management.base import BaseCommand
from insertion_task.models import User, Order, Product
from django.db import IntegrityError


def insert_users():
    user_data = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
        {"name": "David", "email": "david@example.com"},
        {"name": "Eve", "email": "eve@example.com"},
        {"name": "Frank", "email": "frank@example.com"},
        {"name": "Grace", "email": "grace@example.com"},
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Henry", "email": "henry@example.com"},
        {"name": "", "email": "jane@example.com"},
    ]

    for index, user in enumerate(user_data, start=1):
        try:
            if User.objects.using("users").filter(email=user["email"]).exists():
                raise ValueError(f"Duplicate email: {user['email']}")
            if not user["name"]:
                raise ValueError("Name cannot be empty")

            User.objects.using("users").create(**user)
        except (ValueError, IntegrityError) as e:
            print(f"Failed to insert user at index {index}: {e}")


def insert_products():
    product_data = [
        {"name": "Laptop", "price": 1000.00},
        {"name": "Smartphone", "price": 700.00},
        {"name": "Headphones", "price": 150.00},
        {"name": "Monitor", "price": 300.00},
        {"name": "Keyboard", "price": 50.00},
        {"name": "Mouse", "price": 30.00},
        {"name": "Laptop", "price": 1000.00},
        {"name": "Smartwatch", "price": 250.00},
        {"name": "Gaming Chair", "price": 500.00},
        {"name": "Earbuds", "price": -50.00},
    ]
    for index, product in enumerate(product_data, start=1):
        try:
            if Product.objects.using("products").filter(name=product["name"]).exists():
                raise ValueError(f"Duplicate product name: {product['name']}")
            if product["price"] <= 0:
                raise ValueError(f"Price must be positive: {product['price']}")

            Product.objects.using("products").create(**product)
        except (ValueError, IntegrityError) as e:
            print(f"Failed to insert product at index {index}: {e}")


def insert_orders():
    order_data = [
        {"user_id": 1, "product_id": 1, "quantity": 2},
        {"user_id": 2, "product_id": 2, "quantity": 1},
        {"user_id": 3, "product_id": 3, "quantity": 5},
        {"user_id": 4, "product_id": 4, "quantity": 1},
        {"user_id": 5, "product_id": 5, "quantity": 3},
        {"user_id": 6, "product_id": 6, "quantity": 4},
        {"user_id": 7, "product_id": 7, "quantity": 2},
        {"user_id": 8, "product_id": 8, "quantity": 0},
        {"user_id": 9, "product_id": 1, "quantity": 1},
        {"user_id": 10, "product_id": 11, "quantity": 2},
    ]
    for index, order in enumerate(order_data, start=1):
        try:
            if order["quantity"] <= 0:
                raise ValueError(f"Invalid quantity: {order['quantity']}")
            if (
                not Product.objects.filter(id=order["product_id"])
                .using("products")
                .exists()
            ):
                raise ValueError(f"Invalid product_id: {order['product_id']}")

            Order.objects.using("orders").create(**order)
        except (ValueError, IntegrityError) as e:
            print(f"Failed to insert order at index {index}: {e}")


class Command(BaseCommand):
    help = "Simulate simultaneous insertions into multiple SQLite databases"

    def handle(self, *args, **kwargs):
        threads = []
        threads.append(threading.Thread(target=insert_users))
        threads.append(threading.Thread(target=insert_products))
        threads.append(threading.Thread(target=insert_orders))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.stdout.write(
            self.style.SUCCESS("Data inserted successfully into all databases.")
        )
