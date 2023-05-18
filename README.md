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


After clone 


    git clone https://github.com/jesusalc/pizza_django_rest_python.git  pizza_django

run *.sh files
mac be like:

        docker-build.sh
        dpcker-run.sh
        docker-migrate.sh
        docker-test-coverage.sh
        docker-test-bdd.sh

run *.sh files
fedora linux be like:

        docker-build-fedora.sh
        docker-run-fedora.sh
        docker-migrate-fedora.sh
        docker-test-coverage-fedora.sh
        docker-test-bdd-fedora.sh


## or read below for manual  runs

1. Clone the repository:


    on mac
    
    git clone https://github.com/jesusalc/pizza_django_rest_python.git  pizza_django


    on Linux

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


6. Run the migrations to set up the database


    python manage.py migrate

7. Start the Django development server:


    python manage.py runserver

    running on http://localhost:8000 in a production-like environment using  PostgreSQL as the database

    running on http://localhost:8000 in dev mode production-like environment using  Sqlite as the database.

8. Production

    
    Make sure to configure the ALLOWED_HOSTS setting in your settings.py file for the production environment, and consider using environment variables to manage sensitive data like the database credentials.


9. The application is now running on `http://localhost:8000`.

## Testing

    Unit testing 
        docker-test.sh

        python manage.py  test pizza_django/tests
        
    Behave BDD Testing 

        docker-test-bdd.sh

        behave

    Coverage Testing

        docker-test-coverage.sh

        coverage run manage.py test pizza_django/tests && coverage report

## Coverage Unit Testing Report

    Name                                                 Stmts   Miss  Cover
    ------------------------------------------------------------------------
    manage.py                                               12      2    83%
    pizza_django/__init__.py                                 0      0   100%
    pizza_django/migrations/0001_initial.py                  6      0   100%
    pizza_django/migrations/0002_auto_20230516_0500.py       5      0   100%
    pizza_django/migrations/0003_auto_20230516_1030.py       4      0   100%
    pizza_django/migrations/__init__.py                      0      0   100%
    pizza_django/models.py                                  48      6    88%
    pizza_django/serializers.py                             22      5    77%
    pizza_django/settings.py                                18      0   100%
    pizza_django/tests/test_list_orders.py                  27      0   100%
    pizza_django/tests/test_orders.py                       26      0   100%
    pizza_django/tests/test_remove_order.py                 13      0   100%
    pizza_django/tests/test_retrieve_order.py               16      0   100%
    pizza_django/tests/test_update_orders.py                27      0   100%
    pizza_django/urls.py                                     8      0   100%
    pizza_django/views.py                                   12      0   100%
    ------------------------------------------------------------------------
    TOTAL                                                  244     13    95%

## API Endpoints

* `/customers.json` - List all customers or create a new customer
* `/customers/{id}?format=json` - Retrieve, update, or delete a customer by id
* `/pizzas.json` - List all pizzas. Pizzas can only de created with orders.json
* `/pizzas/{id}?format=json` - Retrieve, update, or delete a pizza by id
* `/orders.json` - List all orders or create a new order
* `/orders/{id}/?format=json` - Retrieve, update, or delete an order by id


Look into ./tests-\*.sh below listed, to know how to use the api calls 

    ./test-customers.sh
    ./test-orders.sh
    ./test-pizzas.sh


## Linting


    Make to install all the used packages for linting:

    flake8 black yapf pylint ruff autopep8  oe ohne

    like 
    
    pip install flake8 black yapf pylint ruff autopep8

    or 

    brew install flake8 black yapf pylint ruff autopep8

    oe and ohne install from https://github.com/zeusintuivo/bash_intuivo_cli


    ./fix_lint.sh


## Hooks

    There is pre-commit hook that runs ruff

    


