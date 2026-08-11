from django.urls import path
from . import views


urlpatterns = [

    # Student List
    path(
        "",
        views.student_list,
        name="student_list"
    ),

    # Add Student
    path(
        "add/",
        views.add_student,
        name="add_student"
    ),

    # Edit Student
    path(
        "edit/<int:id>/",
        views.edit_student,
        name="edit_student"
    ),

    # Delete Student
    path(
        "delete/<int:id>/",
        views.delete_student,
        name="delete_student"
    ),

    # Export PDF
    path(
        "export/pdf/",
        views.export_students_pdf,
        name="export_students_pdf"
    ),

    # Export Excel
    path(
        "export/excel/",
        views.export_students_excel,
        name="export_students_excel"
    ),
]