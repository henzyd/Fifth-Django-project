from django.shortcuts import render
from . import models

# Create your views here.
def home_page_func(request):
    articles = models.Article.objects.all()
    # articles = [*articles]
    # articles = articles[::-1]
    context = {
        'articles': articles
    }
    return render(request, 'my_app/articles_folder/home_page.html', context)


def second_page_func(request):
    articles = models.Article.objects.all().last()
    context = {
        'articles': articles
    }
    return render(request, 'my_app/articles_folder/second_page.html', context)