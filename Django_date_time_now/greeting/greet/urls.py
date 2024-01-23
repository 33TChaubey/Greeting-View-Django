from django.urls import path, include
from .views import greeting_view

urlpatterns = [
    path('greeting/',greeting_view,name='greetings')
]