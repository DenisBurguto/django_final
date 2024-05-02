from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('authorization', views.authorization, name='authorization'),
    path('all_receipt', views.all_receipt, name='all_receipt'),
    path('get_receipt', views.get_receipt, name='get_receipt'),
    path('add_receipt', views.add_receipt, name='add_receipt'),
    path('modify_receipt', views.modify_receipt, name='modify_receipt'),
    path('add_receipt/', views.add_receipt, name='add_receipt'),

]
