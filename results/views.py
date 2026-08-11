from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Result
from .forms import ResultForm


def result_list(request):

    search = request.GET.get("search")

    if search:
        results = Result.objects.filter(
            student__first_name__icontains=search
        )
    else:
        results = Result.objects.all().order_by("-id")

    paginator = Paginator(results, 10)

    page = request.GET.get("page")

    results = paginator.get_page(page)

    return render(
        request,
        "results/result_list.html",
        {
            "results": results,
            "search": search
        }
    )


def result_create(request):

    if request.method == "POST":

        form = ResultForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Result Added Successfully"
            )

            return redirect("result_list")

    else:

        form = ResultForm()

    return render(
        request,
        "results/result_form.html",
        {
            "form": form
        }
    )


def result_update(request, pk):

    result = get_object_or_404(Result, pk=pk)

    if request.method == "POST":

        form = ResultForm(
            request.POST,
            instance=result
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Result Updated Successfully"
            )

            return redirect("result_list")

    else:

        form = ResultForm(
            instance=result
        )

    return render(
        request,
        "results/result_form.html",
        {
            "form": form
        }
    )


def result_delete(request, pk):

    result = get_object_or_404(Result, pk=pk)

    if request.method == "POST":

        result.delete()

        messages.success(
            request,
            "Result Deleted Successfully"
        )

        return redirect("result_list")

    return render(
        request,
        "results/result_confirm_delete.html",
        {
            "result": result
        }
    )


def result_detail(request, pk):

    result = get_object_or_404(Result, pk=pk)

    return render(
        request,
        "results/result_detail.html",
        {
            "result": result
        }
    )