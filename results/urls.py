from django.urls import path
from . import views

urlpatterns = [

    path("", views.result_list, name="result_list"),

    path("add/", views.result_create, name="result_add"),

    path("edit/<int:pk>/", views.result_update, name="result_edit"),

    path("delete/<int:pk>/", views.result_delete, name="result_delete"),

    path("detail/<int:pk>/", views.result_detail, name="result_detail"),

]