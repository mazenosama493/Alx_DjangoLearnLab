from rest_framework import serializers
from .models import Author, Book
import datetime
"""
    Serializer for Author model.
    Includes a nested representation of related books using BookSerializer.
    """
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
