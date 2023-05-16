# Pizza Ordering Service

This is a Django-based pizza ordering service using the Django REST framework.

---
# Fullstack Django Application 2023

Welcome to our pizza ordering service, built using the Django REST framework. This application provides a robust set of features that will ensure a smooth pizza ordering experience for customers. This document highlights the functionality and capabilities of our application.

## Functionality Overview

### Order Pizzas:
Our application allows you to place orders for your favourite flavours of pizza - margarita, marinara, salami, in quantities and sizes of your choice (small, medium, large). Each order includes customer information and tracks the status of delivery. Moreover, it is also possible to order the same flavour of pizza in different sizes multiple times.

### Update an Order:
You have the freedom to modify the details of an order — flavours, count, sizes — as per your requirements. However, to maintain the integrity of the delivery process, orders cannot be updated once they have been delivered. The status of delivery can be updated at any point in time.

### Remove an Order:
An order can be removed entirely from the system, providing flexibility in managing your orders.

### Retrieve an Order:
Each order can be fetched individually using its unique identifier, ensuring easy access to order details.

### List Orders:
Our service provides the capability to retrieve all orders at once. Moreover, it offers the ability to filter orders by their status or customer, aiding in efficient order management.

## Implementation Details

1. **Database Structure:** The application uses PostgreSQL as a backend with Django, ensuring efficient data handling and management.

2. **API Design:** The API has been designed and implemented using the Django REST framework, ensuring a robust and reliable service.

3. **Test Coverage:** We have written tests for the API endpoints, ensuring the reliability and robustness of our service.

4. **Docker Setup:** We provide a Docker setup for easy deployment and scalability.

5. **README:** This README contains instructions on how to run the app.

## Technologies Used

This application has been developed using Python 3.8+ and the latest stable releases of Django, Django REST framework etc. We have utilised Django viewsets where possible, maintaining the RESTful nature of our endpoints. The focus of this application is on the structure and data modelling, hence, authentication and frontend UI have not been implemented.

To explore the codebase and understand the inner workings of the application, you can access the public repository where the code has been hosted.

Feel free to reach out if you have any questions or require further information. Happy pizza ordering!

---


## Requirements


## Running the application


run *.sh files 
or read below


1. Clone the repository:


    git clone https://github.com/jesusalc/pizza_django_rest_python.git


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


