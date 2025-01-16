# TradexaTechTask

# Distributed Data Insertion Task

A Django-based project that demonstrates simultaneous data insertion into multiple SQLite databases (`users.db`, `products.db`, `orders.db`). The task uses threading to execute insertions concurrently and includes validations to ensure data integrity.

## Project Structure

C:.
│   .gitignore
│   db.sqlite3
│   manage.py
│   orders.db
│   products.db
│   users.db
│
├───distributed_system
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   
│   
│           
│           
│           
│
└───insertion_task
    │   admin.py
    │   apps.py
    │   db_routers.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
    │
    ├───management
    │   └───commands
    │       │   insert_data.py
    │       
    │       
    │             
    │
    ├───migrations
       │   __init__.py

    


## Overview

This project showcases a method of performing concurrent data insertions into different SQLite databases for users, products, and orders using Python's threading and Django ORM. Key aspects include:

- **SQLite Databases:** `users.db`, `products.db`, `orders.db`.
- **Multi-threading:** The task is run in separate threads to perform concurrent insertions.
- **Data Validation:** Ensures insertions are successful by validating each record before attempting to insert into the database.
  
## Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.12
- Django 5.1
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/HuzaifaAnsari2806/TradexaTechTask.git
    cd TradexaTechTask
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations to set up your databases:

    ```bash
    python manage.py makemigrations
    python manage.py migrate --database=users
    python manage.py migrate --database=orders
    python manage.py migrate --database=products
    ```

4. Run the insertion task using the custom Django management command:

    ```bash
    python manage.py insert_data
    ```

### File Structure

- **`db.sqlite3`:** Main database used by the Django application.
- **`users.db`, `products.db`, `orders.db`:** SQLite databases for user, product, and order data.
- **`insertion_task/management/commands/insert_data.py`:** Custom management command responsible for inserting data into the databases using threads.

## Data Insertion Logic

Data insertion is carried out in three steps:

1. **Insert Users:** Insert a predefined set of users into the `users.db` database.
2. **Insert Products:** Insert a predefined set of products into the `products.db` database.
3. **Insert Orders:** Insert a predefined set of orders, validating product quantities and IDs to ensure data integrity.

### Error Handling & Validation

- **For Users:** Checks if the email is unique. If a user with the same email already exists, the insertion fails.
- **For Products:** Checks for duplicate product names and ensures the price is valid.
- **For Orders:** Validates `product_id` and `quantity`, rejecting orders with invalid data (negative quantities, non-existent product IDs).

## Contributing

If you’d like to contribute to the project, feel free to fork the repository and submit a pull request. Ensure your changes include appropriate tests and follow the code style.

## License

This project is licensed under the MIT License.

---
