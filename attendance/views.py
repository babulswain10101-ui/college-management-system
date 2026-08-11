from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Attendance
from .forms import AttendanceForm


# ==========================================
# ATTENDANCE LIST
# ==========================================

def attendance_list(request):

    search = request.GET.get("search", "").strip()

    attendance = Attendance.objects.select_related(
        "student"
    ).all()

    if search:

        attendance = attendance.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search)
        )

        # Roll number search
        try:
            attendance = Attendance.objects.filter(
                Q(student__first_name__icontains=search) |
                Q(student__last_name__icontains=search) |
                Q(student__roll_number__icontains=search)
            )

        except Exception:
            pass

    attendance = attendance.order_by("-date", "-id")

    paginator = Paginator(attendance, 10)

    page_number = request.GET.get("page")

    attendance = paginator.get_page(page_number)

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance": attendance,
            "search": search,
        }
    )


# ==========================================
# ADD ATTENDANCE
# ==========================================

def attendance_create(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            try:
                form.save()

                messages.success(
                    request,
                    "Attendance marked successfully."
                )

                return redirect("attendance_list")

            except Exception:

                messages.error(
                    request,
                    "Attendance for this student and date already exists."
                )

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "form": form,
            "page_title": "Mark Attendance",
        }
    )


# ==========================================
# UPDATE ATTENDANCE
# ==========================================

def attendance_update(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            try:

                form.save()

                messages.success(
                    request,
                    "Attendance updated successfully."
                )

                return redirect("attendance_list")

            except Exception:

                messages.error(
                    request,
                    "Attendance for this student and date already exists."
                )

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "form": form,
            "page_title": "Edit Attendance",
        }
    )


# ==========================================
# DELETE ATTENDANCE
# ==========================================

def attendance_delete(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == "POST":

        attendance.delete()

        messages.success(
            request,
            "Attendance deleted successfully."
        )

        return redirect("attendance_list")

    return render(
        request,
        "attendance/attendance_confirm_delete.html",
        {
            "attendance": attendance,
        }
    )