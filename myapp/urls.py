from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('articles', views.articles, name="articles"),
    path('activities', views.activities, name="activities"),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]
