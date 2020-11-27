from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  data = {
    'tittle':'Home',
    'halaman':'Home'
  }
  return render(request, 'index.html', data)

def about(request):
  data = {
    'tittle':'About',
    'halaman':'About'
  }
  return render(request, 'about.html', data)