from django.db import models
from base.models import TimeStamped

# Create your models here.


class Graduation(TimeStamped):
    period = models.IntegerField()
    grad_date = models.DateField()
    venue = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Periode Wisuda'
        verbose_name_plural = 'Periode Wisuda'

    def __unicode__(self):
        return "Periode "+str(self.period)


class Student(TimeStamped):
    STUDENT_STATUS = (
        (1, 'Aktif'),
        (2, 'Non Aktif'),
        (3, 'Mangkir'),
        (4, 'Lulus'),
        (5, 'Meninggal'),
    )
    nim = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=200, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STUDENT_STATUS, default=3)
    graduation = models.ForeignKey(Graduation, null=True, blank=True)

    class Meta:
        verbose_name = "Mahasiswa"
        verbose_name_plural = "Mahasiswa"

    def __unicode__(self):
        return self.nim

