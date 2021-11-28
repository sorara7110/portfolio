from django.shortcuts import render
from django.utils import timezone
from .models import Work, Tool


def home(request):
    works = Work.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'portfolio/home.html', {'works': works})

def work_detail(request, pk):
    work = Work.objects.get(pk=pk)
    return render(request, 'portfolio/work_detail.html', {'work': work})