from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'realEstate'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('property_list', views.property_list, name='property_list'),
    path('property/<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('property/<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('property/create', views.property_new, name='property_new'),

    path('admin_home', views.admin_home, name='admin_home'),
    path('property_summary_pdf', views.property_summary_pdf, name='property_summary_pdf'),
]