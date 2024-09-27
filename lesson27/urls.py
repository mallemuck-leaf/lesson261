from django.urls import path
from lesson27 import views

urlpatterns = [
    path('', views.task_page),
    path('task2/', views.product_page, name='list_products'),
    path('task3/', views.add_product, name='add_product'),
]
