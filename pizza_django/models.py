# models.py
# ---

from django.db import models
from django.core.exceptions import ValidationError


class PizzaSize(models.TextChoices):
    SMALL = "SM", "Small"
    MEDIUM = "MD", "Medium"
    LARGE = "LG", "Large"

    class Meta:
        app_label = "pizza_django"


class PizzaFlavor(models.TextChoices):
    MARGARITA = "MG", "Margarita"
    MARINARA = "MR", "Marinara"
    SALAMI = "SL", "Salami"

    class Meta:
        app_label = "pizza_django"


class OrderStatus(models.TextChoices):
    ORDERED = "OD", "Ordered"
    DELIVERED = "DL", "Delivered"

    class Meta:
        app_label = "pizza_django"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        app_label = "pizza_django"


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name="orders")
    status = models.CharField(max_length=46,
                              choices=OrderStatus.choices,
                              default=OrderStatus.ORDERED)

    class Meta:
        app_label = "pizza_django"

    @classmethod
    def remove_order(cls, order_id):
        try:
            order = cls.objects.get(id=order_id)
            order.delete()
            return True
        except cls.DoesNotExist:
            return False


class Pizza(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="pizzas")
    flavor = models.CharField(max_length=46,
                              choices=PizzaFlavor.choices,
                              default=PizzaFlavor.MARGARITA)
    size = models.CharField(max_length=46,
                            choices=PizzaSize.choices,
                            default=PizzaSize.SMALL)
    # count = models.IntegerField()
    count = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.order.status == OrderStatus.DELIVERED:
            raise ValidationError(
                "Cannot modify a pizza associated with a delivered order.")
        super().save(*args, **kwargs)

    class Meta:
        app_label = "pizza_django"


# ---
