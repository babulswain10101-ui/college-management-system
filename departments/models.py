from django.db import models

class Department(models.Model):

    department_name = models.CharField(max_length=100, unique=True)

    department_code = models.CharField(max_length=20, unique=True)

    hod = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name