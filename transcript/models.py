from django.db import models
from department.models import Course
from student.models import Student
# Create your models here.

class Transcript(models.Model):
	grade = models.DecimalField(max_digits=4, decimal_places=2)
	status = models.CharField(max_length=2, default='0')
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)