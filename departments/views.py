from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Department
from .forms import DepartmentForm


# Department List
def department_list(request):

    search = request.GET.get("search")

    if search:
        departments = Department.objects.filter(
            department_name__icontains=search
        )
    else:
        departments = Department.objects.all().order_by("-id")

    paginator = Paginator(departments, 5)
    page = request.GET.get("page")
    departments = paginator.get_page(page)

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
            "search": search,
        }
    )


# Add Department
def department_create(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Department Added Successfully")
            return redirect("department_list")

    else:
        form = DepartmentForm()

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form
        }
    )


# Edit Department
def department_update(request, pk):

    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":

        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            messages.success(request, "Department Updated Successfully")
            return redirect("department_list")

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form
        }
    )


# Delete Department
def department_delete(request, pk):

    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        department.delete()
        messages.success(request, "Department Deleted Successfully")
        return redirect("department_list")

    return render(
        request,
        "departments/department_confirm_delete.html",
        {
            "department": department
        }
    )