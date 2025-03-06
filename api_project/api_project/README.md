# API Authentication and Permissions

## Authentication Setup
This project uses Django REST Framework’s Token Authentication.

### Getting a Token
1. Register a user in Django Admin or via the shell.
2. Retrieve a token using: curl -X POST http://127.0.0.1:8000/api-token-auth/ -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}'

3. Use the token for authentication:curl -X GET http://127.0.0.1:8000/books_all/ -H "Authorization: Token your_token"



### Permission Setup
- All views require authentication (`IsAuthenticated`).
- Unauthorized users receive a **401 Unauthorized** error.

## Endpoints
- **POST** `/api-token-auth/` → Get token
- **GET** `/books_all/` → List all books (requires authentication)
- **POST** `/books_all/` → Create a new book (requires authentication)
- **PUT** `/books_all/<id>/` → Update a book (requires authentication)
- **DELETE** `/books_all/<id>/` → Delete a book (requires authentication)


