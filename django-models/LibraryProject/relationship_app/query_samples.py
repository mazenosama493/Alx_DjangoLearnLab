from relationship_app.models import Book, Author

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books= Book.objects.filter(author=author)
    return books
def get_books_in_library(library_name):
    library=Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_of_library(library):
    librarian = Librarian.objects.get(library=library_name)
    return librarian