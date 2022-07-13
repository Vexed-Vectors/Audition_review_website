
from django.urls import path,include
from index import views

urlpatterns = [
    path('', views.login, name='login' ),
    path('questions/', views.questions, name='questions'),
    path('register', views.register, name='register'),
    
    
]
