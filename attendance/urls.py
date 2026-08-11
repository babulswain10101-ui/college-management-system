from django.urls import path
from . import views


urlpatterns = [

    # Attendance List
    path(
        "",
        views.attendance_list,
        name="attendance_list"
    ),

    # Add Attendance
    path(
        "add/",
        views.attendance_create,
        name="attendance_create"
    ),

    # Edit Attendance
    path(
        "edit/<int:pk>/",
        views.attendance_update,
        name="attendance_update"
    ),

    # Delete Attendance
    path(
        "delete/<int:pk>/",
        views.attendance_delete,
        name="attendance_delete"
    ),
]