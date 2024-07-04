from django.shortcuts import render
from django.views import generic
from .models import booklist

# Create your views here.
class PostList(generic.ListView):
    queryset = booklist.objects.all()
    #template_name = "booklist.html"
    template_name = "main/index.html"
    paginate_by = 6