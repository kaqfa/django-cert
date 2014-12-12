from django.db import models

# Create your models here.


class Student(models.Model):
    STUDENT_STATUS = (
        ('1', 'Aktif'),
        ('2', 'Non Aktif'),
    )
    nim = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    status = models.CharField(max_length=2, options=STUDENT_STATUS)

