Multi Shop

Multi Shop is a multi-functional e-commerce web application built with Django, designed to help users create online stores, add products, and provide a platform for customers to make purchases.
Key Features

    User Registration and Authentication — Users can register and log in to make purchases.
    Product Browsing and Search — Customers can browse and filter products in the catalog.
    Shopping Cart — Users can add selected products to their shopping cart.
    Checkout and Payment System — Enables customers to complete payments for their orders.
    Admin Panel — Store owners can manage products, orders, and users.

Installation

To set up the project locally, follow these steps:

    Clone the repository:

git clone https://github.com/ThompsonShell/multi_shop.git
cd multi_shop

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`

Install required packages:

pip install -r requirements.txt

Configure Environment Variables:

Rename the .env.example file to .env and replace your_secret_key with your actual Django secret key and any other necessary environment-specific values:

SECRET_KEY=your_secret_key

Apply migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the project:

    python manage.py runserver

Usage

After starting the project, you can access the following URLs:

    http://localhost:8000/ - Home page
    http://localhost:8000/admin/ - Admin panel