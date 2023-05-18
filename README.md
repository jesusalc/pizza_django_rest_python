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

# Development


## Running the application



After clone 

on mac

    git clone https://github.com/jesusalc/pizza_django_rest_python.git pizza_django

on Linux using Podman

    git clone https://github.com/jesusalc/pizza_django_rest_python.git

run with *.sh files mac be like


    docker-build.sh
    dpcker-run.sh
    docker-migrate.sh
    docker-test.sh
    docker-test-bdd.sh
    docker-test-coverage.sh
    tests-customers.sh
    tests-customers.sh
    tests-customers.sh
    tests-orders.sh
    tests-orders.sh



run with *.sh files fedora linux be like


    docker-build-fedora.sh
    docker-run-fedora.sh
    docker-migrate-fedora.sh
    docker-test-fedora.sh
    docker-test-bdd-fedora.sh
    docker-test-coverage-fedora.sh
    tests-customers.sh
    tests-customers.sh
    tests-customers.sh
    tests-orders.sh
    tests-orders.sh

---

## or docker manually be like:

1. Clone the repository:

on mac

    git clone https://github.com/jesusalc/pizza_django_rest_python.git  pizza_django
    cd pizza_django


on Linux using Podman

    git clone https://github.com/jesusalc/pizza_django_rest_python.git
    cd pizza_django_rest_python


2. Build and start the application using Docker Compose:
  
on detached

    docker-compose up --build -d

stay on process

    docker-compose up --build


    Find it running on http://localhost:8000 in a production-like environment using  PostgreSQL as the database


3. Run the migrations to set up the database

on mac

    docker-migrate.sh

on Linux using Podman

    docker-migrate-fedora.sh

4. Running the tests

on mac

    docker-test.sh
    docker-test-bdd.sh
    docker-test-coverage.sh

on Linux using Podman

    docker-test-fedora.sh
    docker-test-bdd-fedora.sh
    docker-test-coverage-fedora.sh


## or manually *without* docker be like:

1. Clone

on mac

    git clone https://github.com/jesusalc/pizza_django_rest_python.git  pizza_django
    cd pizza_django


on Linux using Podman

    git clone https://github.com/jesusalc/pizza_django_rest_python.git
    cd pizza_django_rest_python

2. Setup env 

on mac and linux 

    python -m venv venv
    source venv/bin/activate  

on windows 
    
    use 'venv\Scripts\activate'

3. Install the dependencies from the requirements.txt file:

on mac and linux and windows

    pip install -r requirements.txt

4. Start the Django development server:

on mac and linux and windows

    python manage.py runserver

    running on http://localhost:8000 in dev-like environment using Sqlite as the database.

5. Run the migrations to set up the database

on mac and linux and windows

    python manage.py migrate

6. Running the tests

on mac and linux and windows

    python manage.py test test pizza_django/tests

    pip install coverage
    conda install coverage
    
    coverage run manage.py test
    coverage html
    coverage report

6. Develop more unit tests and watch

on mac and linux and windows

    pip install ptw
    conda install ptw
    ptw pizza_django/tests/


# Production

    
    Make sure to configure the ALLOWED_HOSTS setting in your settings.py file for the production environment, and consider using environment variables to manage sensitive data like the database credentials.

    Change the port from 8000 to 80

    Find starter scripts for the follwing Setups:
    
        Docker 
        Kubernetes 
        AWS 
        Serveless 
        Lamba 
        OpenStack 
        Heroku 
        Terraform 
        CircleCI 
        TravisCI 
        GitlabCI 
        Azure 


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

    Curl Testing

        tests-customers.sh
        tests-orders.sh


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


## API Endpoints . *THIS IS NOT STANDARD ROUTE SETUP* 

Rather than using standard route setup for this repo
I opted for using .json function provided by django to use the Smart ViewSets

* `/customers.json` - List all customers or create a new customer
* `/customers/{id}?format=json` - Retrieve, update, or delete a customer by id
* `/pizzas.json` - List all pizzas. Pizzas can only de created with orders.json
* `/pizzas/{id}?format=json` - Retrieve, update, or delete a pizza by id
* `/orders.json` - List all orders or create a new order
* `/orders/{id}/?format=json` - Retrieve, update, or delete an order by id



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




