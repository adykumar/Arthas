from django.shortcuts import render
#from django.http import HttpResponse

posts= [
    {
        'Book':'Harry Potter',
        'Author':'JK Rowling',
        'Genre':'Fantasy'
    },
    {
        'Book':'Around the World in 80 Days',
        'Author':'Jules Verne',
        'Genre': 'Scifi'
    }
]

def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'} )
