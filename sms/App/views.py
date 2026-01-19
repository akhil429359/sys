from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request,'index.html')
def events(request):
    return render(request,'events.html')
def gallery(request):
    return render(request,'gallery.html')

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(name__icontains=query)|Q(course__icontains=query))

    else:
        students = Student.objects.all()
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request,'student_list.html',{"data":data,"query":query})

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
    
def student_detail(request,id):
    data = Student.objects.get(id=id)
    return render(request,'student_detail.html',{"data":data})

