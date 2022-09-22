from django.contrib import admin
from .models import Student_Info,Parent_Info
admin.site.register(Student_Info)
admin.site.register(Parent_Info)


# Register your models here.


# class Admin_connection(admin.ModelAdmin):
#     list_display = ['first_name','last_name','age','DOB','City']


