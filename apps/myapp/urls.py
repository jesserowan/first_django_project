from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.index),
    path('<int:number>/', views.number),
    path('<int:number>/edit/', views.edit),
    path('<int:number>/delete/', views.destroy)
]