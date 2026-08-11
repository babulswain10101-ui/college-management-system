from django.urls import path
from . import views

urlpatterns = [

    path("", views.teacher_list, name="teacher_list"),

    path("add/", views.teacher_create, name="teacher_add"),

    path("edit/<int:pk>/", views.teacher_update, name="teacher_edit"),

    path("delete/<int:pk>/", views.teacher_delete, name="teacher_delete"),
    path("detail/<int:pk>/",views.teacher_detail,name="teacher_detail"),
]