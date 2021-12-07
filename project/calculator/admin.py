from django.contrib import admin
from .models import Csv_read

model_list = [Csv_read,]
admin.site.register(model_list)