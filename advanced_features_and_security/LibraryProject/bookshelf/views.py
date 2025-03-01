from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Article
from django.shortcuts import render
from .models import Book
from django.db.models import Q
from .forms import ExampleForm

def search_books(request):
    title = request.GET.get("title", "")
    books = Book.objects.filter(Q(title__icontains=title))
    return render(request, "bookshelf/book_list.html", {"books": books})


def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})


@login_required
@permission_required('your_app_name.can_view', raise_exception=True)
def article_list(request):
    """View for listing articles (Viewers and above)"""
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})


@login_required
@permission_required('your_app_name.can_create', raise_exception=True)
def article_create(request):
    """View for creating an article (Editors and Admins)"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content, author=request.user)
        return redirect('article_list')
    return render(request, 'articles/create.html')


@login_required
@permission_required('your_app_name.can_edit', raise_exception=True)
def article_edit(request, article_id):
    """View for editing an article (Editors and Admins)"""
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.author:
        return HttpResponseForbidden("You do not have permission to edit this article.")
    
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')

    return render(request, 'articles/edit.html', {'article': article})


@login_required
@permission_required('your_app_name.can_delete', raise_exception=True)
def article_delete(request, article_id):
    """View for deleting an article (Admins only)"""
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_list')



# Create your views here.
