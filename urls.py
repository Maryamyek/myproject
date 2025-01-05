from django.urls import path
from. import views

app_name = 'task'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.list_posts, name='post'),
    path('add/', views.addform, name='form'),
]