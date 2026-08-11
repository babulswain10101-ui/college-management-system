from django.db import models
from departments.models import Department


class Course(models.Model):

    course_name = models.CharField(max_length=100)

    course_code = models.CharField(max_length=20, unique=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    duration = models.CharField(max_length=50)

    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name