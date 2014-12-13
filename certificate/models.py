from django.db import models
from base.models import TimeStamped
from django.contrib.auth.models import User
from student.models import Student

# Create your models here.


class Certificate(TimeStamped):
    certificate_number = models.CharField(max_length=25)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    student = models.ForeignKey(Student)
    thesis_title = models.TextField(blank=True)
    certificate_file = models.FileField(upload_to='certs_file', null=True, blank=True)
    transcript1_file = models.FileField(upload_to='certs_file', null=True, blank=True)
    transcript2_file = models.FileField(upload_to='certs_file', null=True, blank=True)

    class Meta:
        verbose_name = 'Ijazah'
        verbose_name_plural = 'Ijazah'

    def __unicode__(self):
        return self.certificate_number


class Legalization(TimeStamped):
    LEGAL_STATUS = (
        (1, 'Verified'),
        (2, 'In Progress'),
        (3, 'Invalid')
    )

    uploaded_file = models.FileField(upload_to='legalize_file', null=True, blank=True)
    qr_code = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField(choices=LEGAL_STATUS, default=2)
    student = models.ForeignKey(Student, blank=True, null=True)
    submitted_at = models.DateTimeField()
    submitter = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Legalisir'
        verbose_name_plural = 'Legalisir'