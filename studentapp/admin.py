

from django.contrib import admin
from studentapp.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','marks','city', 'mobile']


#admin.site.register(Student,StudentAdmin)

