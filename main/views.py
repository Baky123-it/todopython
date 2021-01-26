from django.shortcuts import render, HttpResponse, render, redirect
from .models import ToDo, Book


# from django.contrib import admin
# from django.urls import path
# from main.views import homepage, test, check
# from django.conf import settings
# from django.conf.urls.static import stati
# Create your views here.

def homepage(request):
    return render( request, "index.html")
 
def test (request):
    todo_list=ToDo.objects.all()
    return render (request, "test.html",{"todo_list": todo_list})

def second(request):
    return HttpResponse ("test 2 page")

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def add_todo (request):
    form = request.POST
    text = form ["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect (test)