from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "first_name",
            "last_name",
            "roll_no",
            "email",
            "phone",
            "gender",
            "department",
            "course",
            "year",
            "photo",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter first name",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter last name",
            }),

            "roll_no": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter roll number",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }),

            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                },
                choices=[
                    ("", "Select Gender"),
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Other", "Other"),
                ],
            ),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter department",
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course",
            }),

            "year": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter year",
            }),

            "photo": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/jpeg,image/png,image/jpg",
            }),
        }