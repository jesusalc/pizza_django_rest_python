touch drinks/models.py
echo "from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=35)

    " > drinks/models.py

python manage.py makemigrations drinks
