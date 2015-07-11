from django.db import models
from testapp.utils import get_upload_file_path
# Create your models here.

class UploadFile(models.Model):
    u_file = models.FileField(upload_to=get_upload_file_path)

    def __unicode__(self):
        return self.u_file