from django.shortcuts import get_object_or_404, render
from models import Content, Article, Company
from pprint import pprint

# Create your views here.
def all_articles(request):
    # Find all blog posts
    data = {'articles': Article.objects.all()}
    return render(request, 'all_articles.html', data)

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    data = {'article': article}
    return render(request, 'article.html', data)