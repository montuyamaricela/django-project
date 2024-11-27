from django.shortcuts import render, get_object_or_404
from .data import ARTICLES  
from .data import multimedia  
from .data import games  

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def articles(request):
    return render(request, 'articles.html', {'items': ARTICLES, 'multimedia': multimedia})

def activities(request):
    return render(request, 'activities.html', {"activities": games})
    

def article_detail(request, slug):
    # Find the article with the matching slug
    article = next((item for item in ARTICLES if item["slug"] == slug), None)

    if not article:
        # If no matching article is found, return a 404 page
        return render(request, "404.html", status=404)

    # Render the article detail page
    return render(request, "article.html", {"article": article, "articles": ARTICLES})