from django.http import HttpResponse
from django.views.decorators.http import require_GET

def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")
@require_GET
def healthcheck(request):
    if request.method == 'GET':
        # Logic to handle the GET request
        return HttpResponse("This is a GET request response.")
    else:
        # Handle other methods or return an error
        return HttpResponse("Method Not Allowed", status=405)