from django.db import models
from students.models import Student
from courses.models import Course


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    semester = models.CharField(max_length=20)

    total_marks = models.PositiveIntegerField()

    obtained_marks = models.PositiveIntegerField()

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False,
        default=0
    )

    grade = models.CharField(
        max_length=2,
        editable=False
    )

    result_date = models.DateField()

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.percentage = (
            self.obtained_marks / self.total_marks
        ) * 100

        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.student)