from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Retain the previous ListAPIView for listing books
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes registered with the router
    path('', include(router.urls)),

]