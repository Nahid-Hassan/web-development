from django.views.generic import ListView
from .models import Post
from django.shortcuts import render


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


def home(request, pk=None, name=None):
    print(pk, name)
    context = {
        'post_titles': Post.objects.all(),
        'post_body': Post.objects.get(pk=pk).body,
    }
    return render(request, 'blog/index.html', context=context)
