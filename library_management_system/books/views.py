from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth import login, authenticate
from .forms import AdminSignupForm
import logging

# Set up logging
logger = logging.getLogger(__name__)



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

class CreateBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_book(request):
    return render(request, 'create_book.html')


class GetAllBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class UpdateBook(APIView):
    def put(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book updated successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update_book(request, book_id):
    return render(request, 'update_book.html', {'book': book})


class DeleteBook(APIView):
    def delete(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully!'})
