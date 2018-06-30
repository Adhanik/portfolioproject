from django.shortcuts import render
from .models import Job #job object so we can access all jobs

def home(request):
    jobs= Job.objects #brings all job object from database and turn them into python objects which can be used inside of our code.
    return render(request,'jobs/home.html', {'jobs': jobs })
