from django.urls import path
from .views import admin_signup, admin_login, CreateBook, GetAllBooks, UpdateBook, DeleteBook

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='admin/signup/', permanent=False), name='home'),
    path('admin/signup/', admin_signup, name='admin_signup'),
    path('admin/login/', admin_login, name='admin_login'),
    path('api/books/create/', CreateBook.as_view(), name='create_book'),
    path('api/books/', GetAllBooks.as_view(), name='book_list'),
    path('api/books/update/<int:book_id>/', UpdateBook.as_view(), name='update_book'),
    path('api/books/delete/<int:book_id>/', DeleteBook.as_view(), name='delete_book'),

]
