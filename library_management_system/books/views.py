from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from django.contrib.auth import login, authenticate
from .forms import AdminSignupForm
import logging

# Set up logging
logger = logging.getLogger(__name__)

def admin_signup(request):
    logger.debug("Accessing admin_signup view")
    
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("New admin user created successfully.")
            return redirect('admin_login')
        else:
            logger.error("Form errors: %s", form.errors)  # Log form errors

    form = AdminSignupForm()  # Always use AdminSignupForm

    return render(request, 'admin_signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
    return render(request, 'admin_login.html')

def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        isbn = request.POST['isbn']
        book = Book(title=title, author=author, published_date=published_date, isbn=isbn)
        book.save()
        return JsonResponse({'message': 'Book created successfully!'})
    return render(request, 'create_book.html')

def get_all_books(request):
    books = Book.objects.all()
    return JsonResponse(list(books.values()), safe=False)

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.save()
        return JsonResponse({'message': 'Book updated successfully!'})
    return render(request, 'update_book.html', {'book': book})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return JsonResponse({'message': 'Book deleted successfully!'})
