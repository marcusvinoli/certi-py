from django.shortcuts import render
from .models import Course
from datetime import datetime

# Create your views here.
def home(request):
	return render(request, 'app/home.html')

def courses(request): 
	if request.method == 'POST':
		new_course = Course() 
		new_course.title = request.POST.get('title')
		new_course.workload = request.POST.get('workload')
		new_course.teacher = request.POST.get('teacher')
		new_course.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
		new_course.save()

	courses = { 'courses': Course.objects.all() }
	
	return render(request, 'app/courses.html', courses)

def templates(request): 
	return render(request, 'app/templates.html')

def settings(request): 
	return render(request, 'app/settings.html')

def certificates(request): 
	return render(request, 'app/certificates.html')