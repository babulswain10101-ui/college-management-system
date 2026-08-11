from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = "__all__"

        widgets = {

            "course_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "course_code": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "department": forms.Select(attrs={
                "class": "form-select"
            }),

            "duration": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "fees": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

        }