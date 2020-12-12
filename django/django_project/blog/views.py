# import render from django.shortcuts
from django.shortcuts import render
from django.http import HttpResponse

# create list of post and each dictionary will be information associated with one post
posts = [
    {
        'author': 'Md. Nahid Hassan',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'December 10, 2020'
    },
    {
        'author': 'Mehedi Hasan Mahin',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December 12, 2020'
    }
]

def home(request):
    context = {
        # key is post and value is our list of posts
        # pass context=context as third argument and 
        # then we are access it using key_name into the template 
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})