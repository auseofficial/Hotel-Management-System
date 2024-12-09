# project_file/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Corrected this line
    path('', include('myapp.urls')),  # Ensure the path is correct
]
