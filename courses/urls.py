from django.urls import path, include

from .views import index, register, speakers

urlpatterns = [
    path('', index),
    path('speakers/', speakers, name='speakers'),
    path('register/<int:pk>/', register, name='course-registration'),
]
