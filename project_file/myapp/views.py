# myapp/views.py

from django.shortcuts import render
from .models import Restaurant  # Correct this line

def restaurant_list(request):
    restaurants = Restaurant.objects.all().values('id', 'name', 'description', 'price', 'created_at')
    return JsonResponse(list(restaurants), safe=False)
