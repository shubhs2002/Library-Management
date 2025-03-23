from django.urls import path
from .views import admin_signup, admin_login, create_book, get_all_books, update_book, delete_book
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='admin/signup/', permanent=False), name='home'),
    path('admin/signup/', admin_signup, name='admin_signup'),
    path('admin/login/', admin_login, name='admin_login'),
    path('books/create/', create_book, name='create_book'),
    path('books/', get_all_books, name='book_list'),
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
