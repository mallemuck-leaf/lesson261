from django.urls import path
from django.views.generic import RedirectView
from lesson27 import views

urlpatterns = [
    path('', RedirectView.as_view(url='task1/', permanent=True)),
    path('task1/', views.task_page, name='start_list'),
    path('task2/', views.product_page, name='list_products'),
    path('task3/', views.add_product, name='add_product'),
]
