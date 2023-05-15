# Pizza Ordering Service

This is a Django-based pizza ordering service using the Django REST framework.

## Requirements
Fullstack Task 2023

Flavors
Imagine a pizza ordering services with the following functionality: • Order pizzas:
• It should be possible to specify the desired flavours of pizza (margarita, marinara, salami), the number of pizzas and their size (small, medium, large).
• An order should contain information regarding the customer.
• It should be possible to track the status of delivery.
• It should be possible to order the same flavour of pizza but with different sizes multiple times

## Running the application

run *.sh files 


1. Clone the repository:


    git clone https://github.com/your-username/pizza_django.git


2. Change into the cloned directory:


    cd pizza_django


3. Build and start the application using Docker Compose:


    docker-compose up --build -d

    docker-compose up --build

4. Running the tests


    python -m venv venv
    source venv/bin/activate  

# On Windows, use 'venv\Scripts\activate'

5. Install the dependencies from the requirements.txt file:


    pip install -r requirements.txt


5. Run the migrations to set up the database


    python manage.py migrate

6. Start the Django development server:


    python manage.py runserver



#  be running on http://localhost:8000 in a production-like environment using Gunicorn and PostgreSQL as the database.

7. Production

    
    Make sure to configure the ALLOWED_HOSTS setting in your settings.py file for the production environment, and consider using environment variables to manage sensitive data like the database credentials.


7. The application is now running on `http://localhost:8000`.

## API Endpoints

* `/customers/` - List all customers or create a new customer
* `/customers/{id}/` - Retrieve, update, or delete a customer by id
* `/pizzas/` - List all pizzas or create a new pizza
* `/pizzas/{id}/` - Retrieve, update, or delete a pizza by id
* `/orders/` - List all orders or create a new order
* `/orders/{id}/` - Retrieve, update, or delete an order by id
* `/order-pizzas/` - List all order-pizza relations or create a new order-pizza relation
* `/order-pizzas/{id}/` - Retrieve, update, or delete an order-pizza relation by id


