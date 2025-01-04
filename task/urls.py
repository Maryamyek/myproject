from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.list_posts, name='post'),
]