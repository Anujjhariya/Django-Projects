from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('abc/',views.morning,name=''),
    path('abcd/',views.good,name=''),
    path('abcde/',views.end,name='')

 
]