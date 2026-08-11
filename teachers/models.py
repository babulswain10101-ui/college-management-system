from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    # Department type karke likhne ke liye
    department = models.CharField(max_length=100)

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField(
        help_text="Experience in Years"
    )

    joining_date = models.DateField()

    photo = models.ImageField(
        upload_to="teachers/",
        blank=True,
        null=True
    )

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"