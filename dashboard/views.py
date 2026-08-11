from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher
from departments.models import Department
from courses.models import Course


def dashboard(request):

    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_departments = Department.objects.count()
    total_courses = Course.objects.count()

    recent_students = Student.objects.order_by("-id")[:5]
    recent_teachers = Teacher.objects.order_by("-id")[:5]

    context = {
        "total_students": total_students,
        "total_teachers": total_teachers,
        "total_departments": total_departments,
        "total_courses": total_courses,

        "recent_students": recent_students,
        "recent_teachers": recent_teachers,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )