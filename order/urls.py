from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'pizza_size', views.SizeViewSet)
router.register(r'pizza_topping', views.ToppingViewSet)
router.register(r'pizza_topping_type', views.ToppingTypeViewSet)
router.register(r'pizza', views.PizzaViewSets)
router.register(r'pizza_order', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
