from django.db import models
from students.models import Student


class Fee(models.Model):

    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("Pending", "Pending"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    payment_method = models.CharField(
        max_length=30,
        default="Cash"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    receipt_number = models.CharField(
        max_length=50,
        unique=True
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student} - {self.amount}"