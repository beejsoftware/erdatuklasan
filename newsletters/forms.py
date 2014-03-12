from django import forms
from newsletters.models import UploadModel


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel