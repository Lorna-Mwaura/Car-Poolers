from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('customer/', views.home, name="home" ),
    path('customer-registration/',views.register,name="customer-registration"),
    path('customer-login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='customer-login'),
    
    
]