from django.contrib import admin

from .models import Book

@admin.register(Book)  # Registers the model with the Django admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    list_filter = ('publication_year', 'author')  # Filters on the right sidebar
    search_fields = ('title', 'author')  # Search bar for quick lookup

# Register your models here.
