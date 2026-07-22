from django.http import HttpResponse

def myFirstProject(request):
    return HttpResponse("Hello World! This is my first Django project.")