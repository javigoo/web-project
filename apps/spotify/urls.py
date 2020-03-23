from django.urls import path, include
from . import views

app_name = 'spotify'
urlpatterns = [
    path('', views.home, name='home'),
    path('top/', views.top_songs, name='topsongs'),
    path('before_log/', views.before_log, name='before_log'),
    path('after_log_<int:id>', views.after_log, name='after_log')
]
