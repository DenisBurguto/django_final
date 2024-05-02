from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('authorization/', views.authorization, name='authorization'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('all_receipt/', views.all_receipt, name='all_receipt'),
    path('get_receipt/', views.get_receipt, name='get_receipt'),
    path('add_receipt/', views.add_receipt, name='add_receipt'),
    path('create_category/', views.create_category, name='create_category'),
    path('receipt_detail/', views.receipt_detail, name='receipt_detail'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('modify_receipt/', views.modify_receipt, name='modify_receipt'),
]
