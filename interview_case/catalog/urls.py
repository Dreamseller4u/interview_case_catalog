from django.urls import path
from . import views

urlpatterns =[
    path('', views.main_view, name='main_view'),
    path('<slug:category_slug>/',views.catalog_view, name='catalog_view'  ),
    path('<slug:category_slug>/<int:id>/',views.catalog_view, name='catalog_view'  ),
]