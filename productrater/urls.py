from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ProductViewSet, RatingViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
