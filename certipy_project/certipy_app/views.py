from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def courses(request): 
    return render(request, 'app/courses.html')

def templates(request): 
    return render(request, 'app/templates.html')

def settings(request): 
    return render(request, 'app/settings.html')

def certificates(request): 
    return render(request, 'app/certificates.html')
