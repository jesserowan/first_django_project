from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def new(request):
    return render(request, 'myapp/new.html')

def create(request):
    return redirect(request, 'myapp/index.html')

def number(request, number):
    return HttpResponse('<h1>Placeholder to display blog number: {}</h1>'.format(number))

def edit(request, number):
    return HttpResponse('<h1>Placeholder to edit blog {}</h1>'.format(number))

def destroy(request, number):
    return redirect('/')