from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
  #return HttpResponse('<html><title>To-Do lists</title><head><h1>To-Do</h1><head></html>')
  return render(request, 'home.html')
