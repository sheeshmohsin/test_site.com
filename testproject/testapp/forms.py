from django.forms import ModelForm
from testapp.models import UploadFile

class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = ['u_file']