# chatgpt/chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_image, name='generate_image'),
]

