from django.contrib import admin
from django.urls import path, include
admin.site.site_header="Hotel Management System"

urlpatterns = [
    path('admin/', admin.site.urls),  # Corrected this line
    path('', include('myapp.urls')),  # Ensure the path is correct
]
