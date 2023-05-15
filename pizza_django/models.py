from django.db import models

class PizzaSize(models.TextChoices):
    SMALL = 'SM', 'Small'
    MEDIUM = 'MD', 'Medium'
    LARGE = 'LG', 'Large'

class PizzaFlavor(models.TextChoices):
    MARGARITA = 'MG', 'Margarita'
    MARINARA = 'MR', 'Marinara'
    SALAMI = 'SL', 'Salami'

class OrderStatus(models.TextChoices):
    ORDERED = 'OD', 'Ordered'
    DELIVERED = 'DL', 'Delivered'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=OrderStatus.choices, default=OrderStatus.ORDERED)

class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=2, choices=PizzaFlavor.choices)
    size = models.CharField(max_length=2, choices=PizzaSize.choices)
    count = models.IntegerField()

class Meta:
    app_label = 'pizza_django'
