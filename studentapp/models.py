
from django.db import models
from django.urls import reverse

class Student(models.Model):
    sname = models.CharField(max_length=30)
    marks = models.IntegerField()
    city = models.CharField(max_length=30)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.sname

    class Meta:
        db_table='student'

    def get_absolute_url(self):
        return reverse('student_list')



