from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from lesson28 import views

urlpatterns = [
    # path('', RedirectView.as_view(url='task1/', permanent=True)),
    path('tasks/', views.task_page, name='task_all'),
    path('tasks/<int:task_id>/', views.show_task, name='task'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
