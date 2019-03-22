from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse




def blog_list(request):
    blogs =  Blog.objects.all().order_by('date')
    return render(request, 'blogs-list.html', {'blogs':blogs})

def blog_details(request, slug):
    #return HttpResponse(slug)
    blog= Blog.objects.get(slug=slug)
    return render(request,'blogs/blog_details.html', {'blog':blog})