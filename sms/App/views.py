from django.shortcuts import render,redirect
from .models import Student
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
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        data = Student.objects.create(name=name,email=email,course=course)
        data.save()
        return redirect(student_list)
    else:
        return render(request,'add_student.html')
    
def update_student(request,id):
    data = Student.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.course = request.POST['course']
        data.save()
        return redirect(student_list)
    else:
        return render(request,'update_student.html',{"data":data})
    
def delete_student(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect(student_list)
    


