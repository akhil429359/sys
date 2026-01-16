from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.

def index(request):
    return render(request,'index.html')
def events(request):
    return render(request,'events.html')
def gallery(request):
    return render(request,'gallery.html')
def student_list(request):
    data = Student.objects.all()
    return render(request,'student_list.html',{"data":data})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request,'add_student.html',{'form':form})
    
def update_student(request,id):
    data = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=data)
    return render(request,'update_student.html',{"form":form})
    
def delete_student(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('student_list')
    


