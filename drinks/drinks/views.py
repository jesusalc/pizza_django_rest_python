from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    drinks = Drink.objects.all()
    serializer_class = DrinkSerializer(drinks,many=True)
    return JsonResponse({"drinks":serializer_class.data}, safe=False)


