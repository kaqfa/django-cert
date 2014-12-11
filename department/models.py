from django.db import models

# Create your models here.

class Department(models.Model):
	DEPT_STATUS = (
			('1', 'Aktif'),
			('0', 'Non Aktif'), 
		)

	code = models.CharField(max_length=5)
	name = models.CharField(max_length=50, verbose_name="Program Studi")
	faculty = models.CharField(max_length=80, verbose_name="Fakultas")
	status = models.CharField(max_length=1, choices=DEPT_STATUS, default='1')


class Course(models.Model):
	COURSE_STATUS = (
			('1', 'Aktif'),
			('0', 'Non Aktif')
		)

	code = models.CharField(max_length=10, verbose_name="Kode Mata Kuliah")
	name = models.CharField(max_length=100, verbose_name="Nama Mata Kuliah")
	status = models.CharField(max_length=1, choices=COURSE_STATUS, default='1')
	department = models.ForeignKey(Department, verbose_name="Fakultas")