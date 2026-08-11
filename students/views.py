from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from openpyxl import Workbook

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm
from .models import Student

from teachers.models import Teacher
from departments.models import Department
from courses.models import Course


# =========================
# HOME
# =========================

def home(request):

    context = {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_departments": Department.objects.count(),
        "total_courses": Course.objects.count(),
    }

    return render(request, "home.html", context)


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    students = Student.objects.all().order_by("-id")

    context = {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_departments": Department.objects.count(),
        "total_courses": Course.objects.count(),

        "students": students,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


# =========================
# STUDENT LIST
# =========================

def student_list(request):

    search = request.GET.get("search", "").strip()

    if search:

        students = Student.objects.filter(
            first_name__icontains=search
        ) | Student.objects.filter(
            last_name__icontains=search
        ) | Student.objects.filter(
            roll_no__icontains=search
        ) | Student.objects.filter(
            email__icontains=search
        )

    else:

        students = Student.objects.all()

    context = {
        "students": students,
        "search": search,
    }

    return render(
        request,
        "students/student_list.html",
        context
    )


# =========================
# ADD STUDENT
# =========================

def add_student(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form
        }
    )


# =========================
# EDIT STUDENT
# =========================

def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "students/edit_student.html",
        {
            "form": form,
            "student": student
        }
    )


# =========================
# DELETE STUDENT
# =========================

def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect("student_list")


# =========================
# EXPORT STUDENTS PDF
# =========================

def export_students_pdf(request):

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'attachment; filename="students.pdf"'
    )

    doc = SimpleDocTemplate(
        response
    )

    data = [
        [
            "ID",
            "Name",
            "Roll No",
            "Email",
            "Phone"
        ]
    ]

    students = Student.objects.all()

    for student in students:

        data.append(
            [
                student.id,

                f"{student.first_name} "
                f"{student.last_name}",

                # IMPORTANT:
                # Model field is roll_no
                student.roll_no,

                student.email,

                student.phone,
            ]
        )

    table = Table(data)

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.blue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.beige
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),
            ]
        )
    )

    doc.build(
        [table]
    )

    return response


# =========================
# EXPORT STUDENTS EXCEL
# =========================

def export_students_excel(request):

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Students"

    worksheet.append(
        [
            "ID",
            "First Name",
            "Last Name",
            "Roll No",
            "Email",
            "Phone",
            "Gender",
            "Department",
            "Course",
            "Year",
        ]
    )

    students = Student.objects.all()

    for student in students:

        worksheet.append(
            [
                student.id,
                student.first_name,
                student.last_name,

                # IMPORTANT:
                # Model field is roll_no
                student.roll_no,

                student.email,
                student.phone,
                student.gender,
                student.department,
                student.course,
                student.year,
            ]
        )

    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-"
            "officedocument.spreadsheetml.sheet"
        )
    )

    response["Content-Disposition"] = (
        'attachment; filename="students.xlsx"'
    )

    workbook.save(response)

    return response