touch drinks/admin.py
echo "from django.contrib import admin
from .models import Drink

admin.site.register(Drink)

" >> drinks/admin.py
echo "RESTART SERVER FOR CHANGES to take effekt"
