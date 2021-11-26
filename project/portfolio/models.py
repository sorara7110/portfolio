from django.conf import settings
from django.db import models
from django.utils import timezone

def get_upload_path(instance, name):
    return f'image/{instance.name}.png'

class Work(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=get_upload_path)
    URL = models.URLField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    introduction = models.TextField()
    explanation = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Tool(models.Model):
    class_name = (("1", "language"),("2", "tool"))
    
    post = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='related_tool')
    tool_name = models.CharField(max_length=100)
    tool_class = models.CharField(max_length=20, choices=class_name)