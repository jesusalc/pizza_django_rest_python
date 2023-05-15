from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'pizzas', views.PizzaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

