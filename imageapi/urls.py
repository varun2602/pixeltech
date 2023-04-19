from django.urls import path 
from . import views 

urlpatterns = [
    path('create_data/', views.create_data, name = 'create_data'),
    path('get_data/', views.get_data, name = 'get_data'),
    path('test', views.test, name = 'test')
]

