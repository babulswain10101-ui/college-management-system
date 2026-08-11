from django import forms
from .models import Fee
from students.models import Student


class FeeForm(forms.ModelForm):

    student = forms.ModelChoiceField(
        queryset=Student.objects.all().order_by("first_name"),
        required=True,
        empty_label="-- Search / Select Student --",
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "id_student",
            }
        )
    )

    class Meta:

        model = Fee

        fields = [
            "student",
            "amount",
            "payment_date",
            "payment_method",
            "status",
            "receipt_number",
            "remarks",
        ]

        widgets = {

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter amount",
                    "step": "0.01",
                }
            ),

            "payment_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "payment_method": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cash / UPI / Card",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "receipt_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter receipt number",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter remarks",
                }
            ),
        }