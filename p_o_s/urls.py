"""
URL configuration for fl_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard_class.as_view(), name='dashboard'),
    
    path('product/', views.product_class.as_view(), name='product'),
    path('product/<str:method>/<int:id>/', views.product_class.as_view(), name='product'),
    path('product/<str:method>/', views.product_class.as_view(), name='product'),
    
    path('customer', views.customer_class.as_view(), name='customer'),
    path('customer-new/<str:method>/', views.customer_class.as_view(), name='customer-new'),
    path('customer-update/<str:method>/<int:id>/', views.customer_class.as_view(), name='customer-update'),
    
    path('stats', views.stats_class.as_view(), name='stats'),
    path('settings', views.settings_class.as_view(), name='settings'),
]
