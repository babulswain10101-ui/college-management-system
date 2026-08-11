from django import forms
from django.db.models import Q

from .models import Attendance
from students.models import Student


class AttendanceForm(forms.ModelForm):

    student_name = forms.CharField(
        label="Student",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Type student name or roll number...",
                "autocomplete": "off",
                "list": "student-list",
            }
        )
    )

    class Meta:

        model = Attendance

        fields = [
            "student_name",
            "date",
            "status",
            "remarks",
        ]

        widgets = {

            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "remarks": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Optional remarks...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Edit attendance ke time existing student name show hoga
        if self.instance and self.instance.pk:

            student = self.instance.student

            if student:

                full_name = (
                    f"{student.first_name} "
                    f"{student.last_name}"
                ).strip()

                self.fields["student_name"].initial = full_name

        # Student suggestions
        self.student_choices = Student.objects.all().order_by(
            "first_name"
        )

    def clean_student_name(self):

        name = self.cleaned_data["student_name"].strip()

        if not name:
            raise forms.ValidationError(
                "Please enter student name."
            )

        # Full name
        parts = name.split()

        if len(parts) >= 2:

            first_name = parts[0]
            last_name = " ".join(parts[1:])

            students = Student.objects.filter(
                first_name__iexact=first_name,
                last_name__iexact=last_name
            )

            if students.count() == 1:
                return students.first()

        # First name / last name search
        students = Student.objects.filter(
            Q(first_name__icontains=name) |
            Q(last_name__icontains=name)
        )

        if students.count() == 1:
            return students.first()

        # Roll number search
        # Agar Student model mein roll_number hai
        try:

            students = Student.objects.filter(
                roll_number__icontains=name
            )

            if students.count() == 1:
                return students.first()

        except Exception:
            pass

        raise forms.ValidationError(
            "Student not found. Please enter the correct student name or roll number."
        )

    def save(self, commit=True):

        attendance = super().save(commit=False)

        attendance.student = self.cleaned_data["student_name"]

        if commit:
            attendance.save()

        return attendance