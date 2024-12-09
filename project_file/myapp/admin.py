# myapp/admin.py

from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at')
    search_fields = ('name', 'description')  # Optional: For better search functionality

admin.site.register(Restaurant, RestaurantAdmin)
