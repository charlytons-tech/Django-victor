from django.http import HttpResponse
from django.views.decorators.http import require_GET

def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")

from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request, *args, **kwargs):
        # Logic to handle the GET request
        return HttpResponse("This is a GET request response.")

    # You can define other methods like post(), put(), etc., here
