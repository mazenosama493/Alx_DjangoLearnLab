from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
