from django.urls import path 
from . import views 

urlpatterns  = [
    path('', views.index, name = 'index'),
    path('login', views.login_view, name = 'login'),
    path('register', views.register_view, name = 'register'),
    path('validate_name', views.validate_name, name = 'validate_name'), 
    path('verify_otp', views.verify_otp, name = 'verify_otp'),
    path('logout', views.logout_view, name = 'logout'),
    path('image', views.image_slider, name = 'image'),
    path('test', views.test, name = 'test'),
    path('result', views.result, name = 'result'),
    path('test_route', views.test_route, name = 'test_route'),
    
]