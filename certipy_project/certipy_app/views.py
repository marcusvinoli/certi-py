from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Course, Student
from django.core.serializers import serialize
from datetime import datetime

# Create your views here.
def home(request):
	return render(request, 'app/home.html')

def students(request): 
	if request.method == 'POST': 
		new_student = Student()
		new_student.name = request.POST.get('name')
		new_student.email = request.POST.get('email')
		new_student.cpf = request.POST.get('cpf')
		new_student.save()
	
	students = { 'students': Student.objects.all() }

	return render(request, 'app/students.html', students)

def student_details(request, student_id): 
	req_student = Student.objects.get(id = student_id)
	if request.method == 'DELETE': 
		Student.objects.delete(id = student_id)
	elif request.method == 'POST': 
		new_student = Student()
		new_student.name = request.POST.get('name')
		new_student.email	= request.POST.get('email')
		new_student.cpf = request.POST.get('cpf')
		new_student.save()
	return students(request)

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

def course_details(request, course_id):
	req_course = Course.objects.get(id = course_id)
	if request.method == 'DELETE': 
		req_course.delete()
		# return HttpResponse("OK")
		return redirect('/')
	elif request.method == 'POST': 
		new_student = Student()
		new_student.name = request.POST.get('name')
		new_student.email	= request.POST.get('email')
		new_student.cpf = request.POST.get('cpf')
		new_student.save()
		req_course.students.add(new_student.id)
		req_course.save()
	elif request.method == 'PATCH': 
		print("{}", request)
	course = { 'course': req_course }
	return render(request, 'app/course_details.html', course)

def templates(request): 
	return render(request, 'app/templates.html')

def settings(request): 
	return render(request, 'app/settings.html')

def certificates(request): 
	return render(request, 'app/certificates.html')

def api_students(request): 
	students = Student.objects.all()
	sanitized_data = [] 
	for student in students: 
		sanitized_data.append({
			'id': student.id,
			'name': student.name,
			'email': student.email,
			'cpf': student.cpf,
		})
	print(sanitized_data)
	data = { 'students': sanitized_data }
	return JsonResponse(data, safe=False)
