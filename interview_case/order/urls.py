from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.view_order_create, name='order_create'),
]