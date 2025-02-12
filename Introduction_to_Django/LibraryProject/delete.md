book.delete()

books = Book.objects.all()
print(books.count())  # Expected Output: 0
