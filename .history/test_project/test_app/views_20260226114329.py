from django.http import HttpResponse
from django.views.decorators.http import require_GET

def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")

class MyView(View):
    def get(self, request, *args, **kwargs):
        # Logic to handle the GET request
        return HttpResponse("This is a GET request response.")