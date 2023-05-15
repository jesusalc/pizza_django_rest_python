touch drinks/views.py
echo "from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer_class = DrinkSerializer(drinks,many=True)
        return JsonResponse({'drinks':serializer_class.data}, safe=False)

    if request.method == 'POST':
        serializer_class = DrinkSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'time':'time', 'msg':serializer_class.data, 'status':'ok'},status=status.HTTP_201_CREATED)



" > drinks/views.py

