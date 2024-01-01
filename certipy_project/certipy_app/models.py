from unittest.util import _MAX_LENGTH
from django.db import models

class Student(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.TextField(max_length = 255)
	email = models.TextField(max_length = 255, unique = True,  null = True, blank = True)
	cpf = models.TextField(max_length = 255, unique = True, null = True, blank = True)

class Course(models.Model): 
	id = models.AutoField(primary_key = True)
	date = models.DateField()
	title = models.TextField(max_length = 255)
	template = models.ForeignKey("Template", on_delete = models.SET_NULL, null = True)
	teacher = models.TextField(max_length = 255)
	workload = models.PositiveIntegerField()
	students = models.ManyToManyField(Student)

class Certificate(models.Model): 
	id = models.AutoField(primary_key = True)
	path = models.TextField(max_length = 255)
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	student = models.ForeignKey(Student, on_delete = models.CASCADE)

class Template(models.Model): 
	id = models.AutoField(primary_key = True)
	name = models.TextField(max_length = 255)
	file = models.FileField(upload_to = 'certipy_templates/user')
	fields = models.TextField(max_length = 255)
