from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("customers", views.customer_view, name="customer-view"),
    path("customers/<int:id>", views.customer_detail, name="customer-detail"),
    path("orders", views.order_view, name="order-view"),
    path("orders/<int:id>", views.order_detail, name="order-detail"),
    path("pizzas", views.pizza_view, name="pizza-view"),
    path("pizzas/<int:id>", views.pizza_detail, name="pizza-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
