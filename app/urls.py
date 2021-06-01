from django.urls import path
from app import views

urlpatterns = [
    path('',views.home ,name = 'home'),
    path('blog/',views.blog,name='blog'),
    path('assignment-help/',views.homework,name='homework-help'),

]
