from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .forms import ArticleForm


@login_required
def index(request):

    list_articles = Article.objects.all()[:10]
    return render(request, 'blog/list_articles.html', {'list_articles': list_articles})


@login_required
def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:list_articles')

    return render(request, 'blog/article_form.html')
