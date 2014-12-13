from django.db import models
from base.models import TimeStamped
from department.models import Course
from student.models import Student
# Create your models here.


class Transcript(TimeStamped):
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=2, default='0')
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)

    class Meta:
        verbose_name = 'Transkrip Nilai'
        verbose_name_plural = 'Transkrip Nilai'

    def char_grade(self):
        if self.grade >= 85:
            return "A"
        elif self.grade >= 70:
            return 'B'
        elif self.grade >= 60:
            return 'C'
        elif self.grade >= 50:
            return 'D'
        else:
            return 'E'

    def __unicode__(self):
        return self.grade+' ('+self.char_grade()+')'

