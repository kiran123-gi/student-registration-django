from django.shortcuts import render,redirect
from application.models import StudentModel
from application.forms import StudentForm
def student(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student1")
    else:
        form = StudentForm()
    return render(request,"frontend/index.html",{'form':form,'student':student})
