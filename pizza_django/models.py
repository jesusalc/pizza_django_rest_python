from django.db import models

class PizzaSize(models.TextChoices):
    SMALL = 'SM', 'Small'
    MEDIUM = 'MD', 'Medium'
    LARGE = 'LG', 'Large'

    class Meta:
        app_label = 'pizza_django'

class PizzaFlavor(models.TextChoices):
    MARGARITA = 'MG', 'Margarita'
    MARINARA = 'MR', 'Marinara'
    SALAMI = 'SL', 'Salami'

    class Meta:
        app_label = 'pizza_django'

class OrderStatus(models.TextChoices):
    ORDERED = 'OD', 'Ordered'
    DELIVERED = 'DL', 'Delivered'

    class Meta:
        app_label = 'pizza_django'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'pizza_django'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=46, choices=OrderStatus.choices, default=OrderStatus.ORDERED)
    
    class Meta:
        app_label = 'pizza_django'

class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pizzas')
    flavor = models.CharField(max_length=46, choices=PizzaFlavor.choices)
    size = models.CharField(max_length=46, choices=PizzaSize.choices)
    count = models.IntegerField()
    
    class Meta:
        app_label = 'pizza_django'
