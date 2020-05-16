from django.shortcuts import render
from .models import Job
def hopg(request):
    a=Job.objects
    return render(request,'jobs/home.html',{'jobs':a})
