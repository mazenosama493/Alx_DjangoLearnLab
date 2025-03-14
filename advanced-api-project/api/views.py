from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of books or create a new one.
    - GET: Returns all books (accessible to everyone).
    - POST: Creates a new book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return []

# Retrieve, update, or delete a book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a book.
    - GET: Retrieve a book (accessible to everyone).
    - PUT/PATCH: Update a book (only for authenticated users).
    - DELETE: Remove a book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return []
