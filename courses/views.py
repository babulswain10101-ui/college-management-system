from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Course
from .forms import CourseForm


def course_list(request):

    search = request.GET.get("search")

    if search:
        courses = Course.objects.filter(
            course_name__icontains=search
        )
    else:
        courses = Course.objects.all().order_by("-id")

    paginator = Paginator(courses, 5)

    page = request.GET.get("page")

    courses = paginator.get_page(page)

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "search": search
        }
    )


def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
            return redirect("course_list")

    else:

        form = CourseForm()

    return render(
        request,
        "courses/course_form.html",
        {
            "form": form
        }
    )


def course_update(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Course Updated Successfully")
            return redirect("course_list")

    else:

        form = CourseForm(instance=course)

    return render(
        request,
        "courses/course_form.html",
        {
            "form": form
        }
    )


def course_delete(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course.delete()
        messages.success(request, "Course Deleted Successfully")
        return redirect("course_list")

    return render(
        request,
        "courses/course_confirm_delete.html",
        {
            "course": course
        }
    )