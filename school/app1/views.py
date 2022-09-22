from django.shortcuts import render
from .models import Student_Info,Parent_Info
from .forms import Student_edit

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

def Student_edit_view(request):
    if request.method=='POST':
        fm=Student_edit(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            ag = fm.cleaned_data['age']
            bd = fm.cleaned_data['DOB']
            ct = fm.cleaned_data['City']
            print("firstname==>",fn)
            print("lastname==>",ln)
            print("age==>",ag)
            print("DOB==>",bd)
            print("City==>",ct)
            reg = Student_Info(first_name=fn,last_name=ln,age=ag,DOB=bd,City=ct)
            print("REg type===>>>>",type(reg))
            reg.save()
            fm = Student_edit()
    else:
        fm = Student_edit()  ## empty form
    # dict = {'form':fm}
    return render(request,'tempapp/Student_edit_html.html',{'form':fm})

def Parent_edit_view(request):
    return render(request,'tempapp/Add_new_parents.html')

