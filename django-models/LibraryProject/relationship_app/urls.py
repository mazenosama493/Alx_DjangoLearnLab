from django.urls import path
from .views import list_books, LibraryDetailView
from .views import home
from django.contrib.auth import views as auth_views
from .views import register
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book


urlpatterns = [
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
