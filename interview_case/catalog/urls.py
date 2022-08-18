from django.urls import path
from . import views

urlpatterns =[
    path('', views.main_view, name='main_view'),
    path('<slug:slug>/', views.catalog_view, name='catalog_view')
]