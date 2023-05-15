touch drinks/views.py
echo "from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer_class = DrinkSerializer(drinks,many=True)
        return Response({'drinks':serializer_class.data})

    if request.method == 'POST':
        serializer_class = DrinkSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'time':'time', 'msg':serializer_class.data, 'status':'ok'},status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_details(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_class = DrinkSerializer(drink)
        return Response(serializer_class.data)
    elif request.method == 'PUT':
        serializer_class = DrinkSerializer(drink, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



" > drinks/views.py

