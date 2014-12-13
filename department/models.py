from django.db import models
from base.models import TimeStamped

# Create your models here.


class Department(TimeStamped):
    DEPT_STATUS = (
        (1, 'Aktif'),
        (0, 'Non Aktif'),
    )

    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50, verbose_name="Program Studi")
    faculty = models.CharField(max_length=80, verbose_name="Fakultas")
    status = models.PositiveSmallIntegerField(choices=DEPT_STATUS, default='1')

    class Meta:
        verbose_name = 'Program Studi'
        verbose_name_plural = 'Program Studi'

    def __unicode__(self):
        return self.name


class Course(TimeStamped):
    COURSE_STATUS = (
        (1, 'Aktif'),
        (0, 'Non Aktif')
    )

    code = models.CharField(max_length=10, verbose_name="Kode Mata Kuliah")
    name = models.CharField(max_length=100, verbose_name="Nama Mata Kuliah")
    status = models.PositiveSmallIntegerField(choices=COURSE_STATUS, default='1')
    department = models.ForeignKey(Department, verbose_name="Fakultas")

    class Meta:
        verbose_name = 'Mata Kuliah'
        verbose_name_plural = 'Mata Kuliah'

    def __unicode__(self):
        return self.name