from django.contrib import admin
from .models import Work, Tool

model_list = [Work, Tool]
admin.site.register(model_list)