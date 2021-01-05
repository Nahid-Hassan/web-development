from django.shortcuts import render


def index(request):
    context = {
        'title': 'Index Page',
        'body': "Index body text",
    }
    return render(request, 'blog/index.html', context=context)


def tutorial(request):
    context = {
        'title': 'Tutorial Page',
        'body': "Tutorial body text",
    }
    return render(request, 'blog/tutorial.html', context=context)
