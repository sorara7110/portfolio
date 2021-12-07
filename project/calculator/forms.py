from django import forms
from .models import Csv_read

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Csv_read
        fields = ("file",)