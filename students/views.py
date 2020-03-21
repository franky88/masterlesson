from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentName
from .forms import StudentAddForm
# Create your views here.
def student_list(request):
    student_list = StudentName.objects.all().order_by("-timestamp")
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
    