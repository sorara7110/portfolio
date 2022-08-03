from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

class Csv_read(models.Model):
    file = models.FileField(upload_to='csv', validators=[FileExtensionValidator(['csv'])])

    def publish(self):
        self.save()

    class Meta:
        app_label = 'calculator'

    def __str__(self):
        return self.file.url