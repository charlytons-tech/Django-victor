from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")