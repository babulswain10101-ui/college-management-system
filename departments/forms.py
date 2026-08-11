from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = "__all__"

        widgets = {

            "department_name": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "department_code": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "hod": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "description": forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            }),

        }