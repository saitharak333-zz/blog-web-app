from django.shortcuts import render, redirect
from .models import Article
# Importing Article model to view on the Articles page.
from django.http import HttpResponse
# Importing decorators to ensure user based functionality.
from django.contrib.auth.decorators import login_required
# Importing our costomised form
from . import forms

# Create your views here.
def articleList(request):
    articles_all = Article.objects.all().order_by('date')
    # All the articles stored in the database are called and ordered by dates.
    return render(request, 'article/articleList.html', {'articles_all': articles_all})

def details(request, pagename):
    article_d = Article.objects.get(slug=pagename)
    return render(request, 'article/articleDetail.html', {'article_d':article_d})

@login_required(login_url='users:login')
def create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('article:arlist')
    else:
        form = forms.CreateArticle()
    return render(request, 'article/createArticle.html', {'form':form})

def aboutDesigner(request):
    return render(request, 'article/aboutDesigner.html')

def contactDesigner(request):
    return render(request, 'article/contact.html')
