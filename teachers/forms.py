from django import forms
from .models import Teacher
from departments.models import Department

class TeacherForm(forms.ModelForm):

    department = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Department Name"
        })
    )

    class Meta:
        model = Teacher

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "department",
            "qualification",
            "experience",
            "joining_date",
            "photo",
            "address",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "qualification": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Qualification"
            }),

            "experience": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Experience (Years)"
            }),

            "joining_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Address"
            }),
        }

    def clean_department(self):
        department_name = self.cleaned_data["department"]

        try:
            return Department.objects.get(department_name=department_name)
        except Department.DoesNotExist:
            raise forms.ValidationError(
                "Department not found. Please enter a valid department name."
            )