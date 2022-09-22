from django.shortcuts import render
from .models import Student_Info,Parent_Info

# Create your views here.

def show_details(request):
    data = Student_Info.objects.all()
    dict = {'data':data}
    return render(request,'tempapp/Show_Student_details.html',context=dict)

def Parent_deatils(request):
    data = Parent_Info.objects.all()
    print("Data=====>",data)
    # print("sql_querry======>",data.query)
    dict = {'data':data}
    return render(request,'tempapp/Parent_info.html',context=dict)
