from django.urls import path
from whatsapp_app import views

urlpatterns = [
    path('',views.home),
    path('SendData',views.SendData,name='sendData'),
]

