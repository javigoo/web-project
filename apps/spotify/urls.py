from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'spotify'
urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),

    path('', views.home, name='home'),
    path('top/', views.top_songs, name='topsongs'),
]
