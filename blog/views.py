from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import blog
from django.urls import reverse_lazy

# Create your views here.

class post_list(ListView):
    queryset = blog.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

class post_detail(DetailView):
    model = blog
    template_name = 'detail.html'
    context_object_name = 'post'

class blog_create(CreateView):
    model = blog
    fields = '__all__'
    template_name = 'blog_create.html'
    success_url = reverse_lazy('post_list')
