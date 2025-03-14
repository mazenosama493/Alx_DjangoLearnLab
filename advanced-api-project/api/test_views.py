from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data for Book API"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author
        )
        self.client.login(username="testuser", password="testpass")
        self.book_list_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter and the Sorcerer's Stone")

    def test_create_book(self):
        """Test creating a new book"""
        new_book = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, new_book, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating a book"""
        updated_data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(f"{self.book_list_url}?title=Harry Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_search_books(self):
        """Test searching books by keyword"""
        response = self.client.get(f"{self.book_list_url}?search=Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_order_books_by_title(self):
        """Test ordering books by title"""
        response = self.client.get(f"{self.book_list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_permissions(self):
        """Test that unauthorized users cannot create or delete books"""
        self.client.logout()
        response = self.client.post(self.book_list_url, {"title": "New Book"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
