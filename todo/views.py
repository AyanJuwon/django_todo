from django.shortcuts import render, redirect
import requests as request
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.


def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, "todo/todo.html")


def insert_todo_item(request: HttpRequest):
    todo = Todo(content = request.POST["content"])
    todo.save()
    return redirect("todo/list") 

def delete_todo_item(request,todo_id):
    todo_delete = Todo.objects.get(id = todo_id)
    todo_delete.delete()
    return redirect('todo/todo')

