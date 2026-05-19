from django.urls import path, include
from biblioteca.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('biblioteca.urls')),
]