from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books
class ListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    - GET: Returns all books (accessible to everyone).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Update an existing book
class UpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    - PUT/PATCH: Updates a book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete an existing book
class DeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    - DELETE: Removes a book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
