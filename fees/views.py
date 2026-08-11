from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Fee
from .forms import FeeForm


def fee_list(request):

    search = request.GET.get("search")

    if search:
        fees = Fee.objects.filter(
            student__first_name__icontains=search
        )
    else:
        fees = Fee.objects.all().order_by("-id")

    paginator = Paginator(fees, 10)

    page = request.GET.get("page")

    fees = paginator.get_page(page)

    return render(
        request,
        "fees/fee_list.html",
        {
            "fees": fees,
            "search": search,
        }
    )

def fee_create(request):

    if request.method == "POST":

        form = FeeForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Fee Added Successfully"
            )

            return redirect("fee_list")

    else:
        form = FeeForm()

    return render(
        request,
        "fees/fee_form.html",
        {
            "form": form
        }
    )


def fee_update(request, pk):

    fee = get_object_or_404(Fee, pk=pk)

    if request.method == "POST":

        form = FeeForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Fee Updated Successfully"
            )

            return redirect("fee_list")

    else:

        form = FeeForm(
            instance=fee
        )

    return render(
        request,
        "fees/fee_form.html",
        {
            "form": form
        }
    )


def fee_delete(request, pk):

    fee = get_object_or_404(
        Fee,
        pk=pk
    )

    if request.method == "POST":

        fee.delete()

        messages.success(
            request,
            "Fee Deleted Successfully"
        )

        return redirect("fee_list")

    return render(
        request,
        "fees/fee_confirm_delete.html",
        {
            "fee": fee
        }
    )


def fee_receipt(request, pk):

    fee = get_object_or_404(
        Fee,
        pk=pk
    )

    return render(
        request,
        "fees/receipt.html",
        {
            "fee": fee
        }
    )