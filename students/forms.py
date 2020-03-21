from django import forms
from .models import StudentName
class StudentAddForm(forms.ModelForm):
    class Meta:
        model = StudentName
        fields = (
            "f_name",
            "m_name",
            "l_name",
            "e_name",
            "birth_date",
        )