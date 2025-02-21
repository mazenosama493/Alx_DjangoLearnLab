# CRUD Operations for Book Model in Django

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
Expected Output:
1984

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
Expected Output:
1984 George Orwell 1949

book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
Expected Output:
Nineteen Eighty-Four

book.delete()
books = Book.objects.all()
print(books.count())
Expected Output:
0
