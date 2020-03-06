from django.shortcuts import render, HttpResponse

def index(request): 
    return HttpResponse("placeholder to display a new form to create a new blog") 

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("placeholder to display blog {number}")

def edit(request, number):
    return HttpResponse("placeholder to display blog {number}")

def destroy(request):
    return redirect("/")