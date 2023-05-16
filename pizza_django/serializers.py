from rest_framework import serializers
from .models import Customer, Order, Pizza


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ["flavor", "size", "count"]


class OrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "status", "pizzas"]

    def create(self, validated_data):
        pizzas_data = validated_data.pop("pizzas")
        order = Order.objects.create(**validated_data)
        for pizza_data in pizzas_data:
            Pizza.objects.create(order=order, **pizza_data)
        return order


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = ["id", "name", "address", "orders"]
