from django.urls import path
from . import views

urlpatterns = [

    # Fee List
    path(
        "",
        views.fee_list,
        name="fee_list"
    ),

    # Add Fee
    path(
        "add/",
        views.fee_create,
        name="fee_create"
    ),

    # Edit Fee
    path(
        "edit/<int:pk>/",
        views.fee_update,
        name="fee_update"
    ),

    # Delete Fee
    path(
        "delete/<int:pk>/",
        views.fee_delete,
        name="fee_delete"
    ),

    # Receipt
    path(
        "receipt/<int:pk>/",
        views.fee_receipt,
        name="fee_receipt"
    ),
]