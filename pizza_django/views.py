from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Order, Pizza
from .serializers import CustomerSerializer, OrderSerializer, PizzaSerializer


@api_view(["GET", "POST"])
def customer_view(request, format=None):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer_class = CustomerSerializer(customers, many=True)
        return Response({"customers": serializer_class.data})

    if request.method == "POST":
        serializer_class = CustomerSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                {
                    "time": "time",
                    "msg": serializer_class.data,
                    "status": "ok"
                },
                status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def customer_detail(request, id, format=None):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer_class = CustomerSerializer(customer)
        return Response(serializer_class.data)
    elif request.method == "PUT":
        serializer_class = CustomerSerializer(customer, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def order_view(request, format=None):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer_class = OrderSerializer(orders, many=True)
        return Response({"orders": serializer_class.data})

    if request.method == "POST":
        serializer_class = OrderSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                {
                    "time": "time",
                    "msg": serializer_class.data,
                    "status": "ok"
                },
                status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, id, format=None):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer_class = OrderSerializer(order)
        return Response(serializer_class.data)
    elif request.method == "PUT":
        serializer_class = OrderSerializer(order, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def pizza_view(request, format=None):
    if request.method == "GET":
        pizzas = Pizza.objects.all()
        serializer_class = PizzaSerializer(pizzas, many=True)
        return Response({"pizzas": serializer_class.data})

    # if request.method == "POST":
    #     serializer_class = PizzaSerializer(data=request.data)
    #     if serializer_class.is_valid():
    #         serializer_class.save()
    #         return Response(
    #             {
    #                 "time": "time",
    #                 "msg": serializer_class.data,
    #                 "status": "ok"
    #             },
    #             status=status.HTTP_201_CREATED)
    #     return Response(serializer_class.errors,
    #                     status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def pizza_detail(request, id, format=None):
    try:
        pizza = Pizza.objects.get(pk=id)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer_class = PizzaSerializer(pizza)
        return Response(serializer_class.data)
    elif request.method == "PUT":
        serializer_class = PizzaSerializer(pizza, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)
