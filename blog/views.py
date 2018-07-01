from django.shortcuts import render
from .models import Blog
def allblogs(request):
    blogs=Blog.objects#same name as object to which u are assigning
    return render(request,'blog/allblogs.html',{'blogs':blogs})
