from django.urls import path
from . import views

urlpatterns = [
    path('gato', views.gato, name='gato'),

]