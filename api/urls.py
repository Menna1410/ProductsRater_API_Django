from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProductViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('ratings', RatingViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]