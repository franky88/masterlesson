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

class StudentEditForm(forms.ModelForm):
    # f_name = forms.CharField(max_length=60)
    # m_name = forms.CharField(max_length=60)
    # l_name = forms.CharField(max_length=60)
    # e_name = forms.CharField(max_length=60)
    # birth_date = forms.DateField()
    # disability = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple, 
    #     required=True,
    #     )
    # f_name = forms.CharField(max_length=60)
    class Meta:
        model = StudentName
        fields = (
            "f_name",
            "m_name",
            "l_name",
            "e_name",
            "birth_date",
            "disability",
            "school_status",
            "block",
        )