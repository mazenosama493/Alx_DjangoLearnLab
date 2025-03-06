from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
import rest_framework.generics as generics

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



