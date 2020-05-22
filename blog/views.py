from django.shortcuts import render,get_object_or_404
from .models import Blog

def show(request):
    j=Blog.objects
    return render(request,'blog/show.html',{'blo':j})
def detail(request,blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id)
    return render(request,'blog/detail.html',{'singular':detailblog})
