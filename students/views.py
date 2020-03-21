from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import StudentName
from .forms import StudentAddForm, StudentEditForm
# Create your views here.
def student_list(request):
    student_list = StudentName.objects.all()
    context = {
        "title": "student list",
        "studentlist": student_list,
    }
    return render(request, "students/student_list.html", context)
def student_detail(request, pk):
	student_instance = get_object_or_404(StudentName, pk=pk)
	context = {
		"title": "student details",
		"instance": student_instance,
	}
	return render(request, "students/student_detail.html", context)
def student_add(request):
    form = StudentAddForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect("student:list")
    context = {
        "title": "register student",
        "form": form,
    }
    return render(request, "students/student_add.html", context)
def student_edit(request, pk):
	instance=get_object_or_404(StudentName, pk=pk)
	form = StudentEditForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:list')
	context = {
		"form": form,
		"title": "edit student",
		"instance": instance,
	}
	return render(request, "students/student_edit.html", context)