from django.shortcuts import render

from app.forms import StudentForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Student data submitted")
        else:
            context = {
                "student_form": student_form
            }
            return render(request, "index.html", context=context)
    student_form = StudentForm()
    context = {
        "student_form": student_form
    }
    return render(request, "index.html", context=context)