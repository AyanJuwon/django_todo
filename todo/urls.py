from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
   
    path('', views.list_todo_items,name = 'index'),
    path('insert_todo/', views.insert_todo_item,name = 'insert_todo_item'),
    path('delete_todo/<int:todo_id>', views.delete_todo_item,name = 'delete_todo_item'),
]
