from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Teacher
from .forms import TeacherForm


# Teacher List
def teacher_list(request):

    search = request.GET.get("search")

    if search:
        teachers = Teacher.objects.filter(first_name__icontains=search)
    else:
        teachers = Teacher.objects.all().order_by("-id")

    paginator = Paginator(teachers, 5)
    page_number = request.GET.get("page")
    teachers = paginator.get_page(page_number)

    return render(request, "teachers/teacher_list.html", {
        "teachers": teachers,
        "search": search,
    })


# Add Teacher
def teacher_create(request):

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Teacher Added Successfully")
            return redirect("teacher_list")

    else:
        form = TeacherForm()

    return render(request, "teachers/teacher_form.html", {
        "form": form
    })


# Edit Teacher
def teacher_update(request, pk):

    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)

        if form.is_valid():
            form.save()
            messages.success(request, "Teacher Updated Successfully")
            return redirect("teacher_list")

    else:
        form = TeacherForm(instance=teacher)

    return render(request, "teachers/teacher_form.html", {
        "form": form
    })


# Delete Teacher
def teacher_delete(request, pk):

    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        teacher.delete()
        messages.success(request, "Teacher Deleted Successfully")
        return redirect("teacher_list")

    return render(
        request,
        "teachers/teacher_confirm_delete.html",
        {"teacher": teacher}
    )
    
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    return render(
        request,
        "teachers/teacher_detail.html",
        {
            "teacher": teacher
        }
    )