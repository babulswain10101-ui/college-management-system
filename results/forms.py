from django import forms
from .models import Result
from students.models import Student
from courses.models import Course


class ResultForm(forms.ModelForm):

    student_name = forms.CharField(
        label="Student Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Type student full name"
        })
    )

    class Meta:
        model = Result

        fields = [
            "student_name",
            "course",
            "semester",
            "total_marks",
            "obtained_marks",
            "result_date",
            "remarks",
        ]

        widgets = {

            "course": forms.Select(attrs={
                "class": "form-select"
            }),

            "semester": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: 4th Semester"
            }),

            "total_marks": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Total marks"
            }),

            "obtained_marks": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Obtained marks"
            }),

            "result_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Remarks"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Edit karte time existing student name dikhayega
        if self.instance and self.instance.pk:
            student = self.instance.student

            self.fields["student_name"].initial = (
                f"{student.first_name} {student.last_name}"
            )

    def clean_student_name(self):

        name = self.cleaned_data["student_name"].strip()

        parts = name.split()

        if len(parts) < 2:
            raise forms.ValidationError(
                "Please enter student's full name."
            )

        first_name = parts[0]
        last_name = " ".join(parts[1:])

        student = Student.objects.filter(
            first_name__iexact=first_name,
            last_name__iexact=last_name
        ).first()

        if not student:
            raise forms.ValidationError(
                "Student not found. Please enter an existing student's full name."
            )

        return name

    def save(self, commit=True):

        result = super().save(commit=False)

        name = self.cleaned_data["student_name"].strip()

        parts = name.split()

        first_name = parts[0]
        last_name = " ".join(parts[1:])

        student = Student.objects.filter(
            first_name__iexact=first_name,
            last_name__iexact=last_name
        ).first()

        result.student = student

        if commit:
            result.save()

        return result