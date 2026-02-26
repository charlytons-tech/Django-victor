from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")

def my_view(request):
    if request.method == 'GET':
        # Logic to handle the GET request
        return HttpResponse("This is a GET request response.")
    else:
        # Handle other methods or return an error
        return HttpResponse("Method Not Allowed", status=405)
def healthcheck(request):
    return HttpResponse("health check")