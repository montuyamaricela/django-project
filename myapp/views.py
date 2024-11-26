from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def articles(request):
    return render(request, 'articles.html')

def activities(request):
    return render(request, 'activities.html')
    
def multimedia(request):
    return render(request, 'multimedia.html')