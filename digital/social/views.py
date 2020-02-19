from django.shortcuts import render

posts = [
    {
        'author': 'DevP',
        'title': 'app post 1',
        'content': 'post 1 content',
        'date_posted': 'Dec 3,2020'

    },
    {
        'author': 'DSP',
        'title': 'app post 2',
        'content': 'post 2 content',
        'date_posted': 'Dec 8,2020'

    },

]

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'social/home.html', context)

def about(request):
    return render(request, 'social/about.html', {'title': 'about'})
